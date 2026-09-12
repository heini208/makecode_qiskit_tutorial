import io
import os

import imageio.v2 as imageio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import qutip

matplotlib.use("Agg")

AXIS_COLORS = {
    "x": "#F2C94C",
    "y": "#4A90E2",
    "z": "#27AE60",
}

STATE_COLOR = "purple"


def rx(theta):
    return (-1j * theta / 2 * qutip.sigmax()).expm()


def ry(theta):
    return (-1j * theta / 2 * qutip.sigmay()).expm()


def rz(theta):
    return (-1j * theta / 2 * qutip.sigmaz()).expm()


H = qutip.Qobj(np.array([[1, 1], [1, -1]]) / np.sqrt(2))
X = qutip.sigmax()
Y = qutip.sigmay()


def gate_to_axis_angle(gate):
    matrix = gate.full() if isinstance(gate, qutip.Qobj) else np.asarray(gate, dtype=complex)
    det_phase = np.angle(np.linalg.det(matrix))
    matrix = np.exp(-1j * det_phase / 2) * matrix
    cos_half_angle = np.clip(np.real(np.trace(matrix)) / 2, -1.0, 1.0)
    angle = 2 * np.arccos(cos_half_angle)
    sin_half_angle = np.sin(angle / 2)
    if np.isclose(sin_half_angle, 0):
        return np.array([0.0, 0.0, 1.0]), 0.0
    paulis = [qutip.sigmax().full(), qutip.sigmay().full(), qutip.sigmaz().full()]
    axis = np.array([
        np.real(1j * np.trace(sigma @ matrix) / (2 * sin_half_angle))
        for sigma in paulis
    ])
    return axis / np.linalg.norm(axis), angle


def axis_operator(axis_name):
    return {
        "x": qutip.sigmax(),
        "y": qutip.sigmay(),
        "z": qutip.sigmaz(),
    }[axis_name]


def state_to_bloch_vector(state):
    return np.array([
        np.real(qutip.expect(qutip.sigmax(), state)),
        np.real(qutip.expect(qutip.sigmay(), state)),
        np.real(qutip.expect(qutip.sigmaz(), state)),
    ])


def interpolate_gate_on_state(gate, start_state, num_frames):
    axis, angle = gate_to_axis_angle(gate)
    generator = axis[0] * qutip.sigmax() + axis[1] * qutip.sigmay() + axis[2] * qutip.sigmaz()
    states = []
    for current_angle in np.linspace(0, angle, num_frames):
        unitary = (-1j * current_angle / 2 * generator).expm()
        states.append(unitary * start_state)
    return states, gate * start_state


def interpolate_axis_rotation(axis_name, angle, start_state, num_frames):
    generator = axis_operator(axis_name)
    states = []
    for current_angle in np.linspace(0, angle, num_frames):
        unitary = (-1j * current_angle / 2 * generator).expm()
        states.append(unitary * start_state)
    return states, states[-1]


def create_bloch_frame(state, trajectory_segments=None):
    bloch = qutip.Bloch()
    bloch.vector_color = [STATE_COLOR]
    bloch.zlabel = ["z $|0\\rangle$", "$|1\\rangle$"]
    bloch.add_states(state)
    if trajectory_segments:
        for segment in trajectory_segments:
            points = np.asarray(segment["points"])
            if len(points) < 2:
                continue
            bloch.add_points(
                points.T,
                meth="l",
                colors=[segment["color"]],
                alpha=1.0,
                linewidth=3,
            )
    bloch.make_sphere()
    return bloch


def save_gif(states, segments, output_path, frame_duration):
    trajectory = []
    frames = []
    for frame_index, state in enumerate(states):
        trajectory.append(state_to_bloch_vector(state))
        visible_segments = []
        for segment in segments:
            start = segment["start"]
            end = min(segment["end"], frame_index + 1)
            if end - start >= 2:
                visible_segments.append({
                    "points": trajectory[start:end],
                    "color": segment["color"],
                })
        bloch = create_bloch_frame(state, visible_segments)
        buffer = io.BytesIO()
        bloch.fig.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0.1)
        buffer.seek(0)
        frames.append(imageio.imread(buffer))
        buffer.close()
        plt.close(bloch.fig)
    imageio.mimsave(output_path, frames, duration=frame_duration, loop=0)


def create_gate_gif(gate, name, output_dir, initial_state=None, num_frames=30, frame_duration=0.12, path=None):
    if initial_state is None:
        initial_state = qutip.basis(2, 0)
    all_states = []
    segments = []
    current_state = initial_state
    if path is None:
        states, _ = interpolate_gate_on_state(gate, current_state, num_frames)
        axis, _ = gate_to_axis_angle(gate)
        dominant_axis = ("x", "y", "z")[int(np.argmax(np.abs(axis)))]
        all_states.extend(states)
        segments.append({
            "start": 0,
            "end": len(states),
            "color": AXIS_COLORS[dominant_axis],
        })
    else:
        for operation_index, (axis_name, angle) in enumerate(path):
            states, final_state = interpolate_axis_rotation(axis_name, angle, current_state, num_frames)
            if operation_index > 0:
                states = states[1:]
            start_index = len(all_states)
            all_states.extend(states)
            segments.append({
                "start": start_index,
                "end": len(all_states),
                "color": AXIS_COLORS[axis_name],
            })
            current_state = final_state
    save_gif(all_states, segments, os.path.join(output_dir, f"{name}.gif"), frame_duration)


def create_gate_sequence_gif(operations, name, output_dir, initial_state=None, num_frames_per_op=25, frame_duration=0.12):
    if initial_state is None:
        initial_state = qutip.basis(2, 0)
    all_states = []
    segments = []
    current_state = initial_state
    for operation_index, operation in enumerate(operations):
        kind = operation[0]
        if kind == "gate":
            gate = operation[1]
            states, final_state = interpolate_gate_on_state(gate, current_state, num_frames_per_op)
            axis, _ = gate_to_axis_angle(gate)
            color = AXIS_COLORS[("x", "y", "z")[int(np.argmax(np.abs(axis)))]]
        else:
            axis_name = operation[1]
            angle = operation[2]
            states, final_state = interpolate_axis_rotation(axis_name, angle, current_state, num_frames_per_op)
            color = AXIS_COLORS[axis_name]
        if operation_index > 0:
            states = states[1:]
        start_index = len(all_states)
        all_states.extend(states)
        segments.append({
            "start": start_index,
            "end": len(all_states),
            "color": color,
        })
        current_state = final_state
    save_gif(all_states, segments, os.path.join(output_dir, f"{name}.gif"), frame_duration)


def main():
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    create_gate_gif(H, "hadamard_diagonal", output_dir)
    create_gate_gif(X, "x_gate", output_dir)
    create_gate_gif(Y, "y_gate", output_dir)
    create_gate_gif(rx(np.pi / 2), "rx_pi_2", output_dir)
    create_gate_gif(ry(np.pi / 2), "ry_pi_2", output_dir)
    create_gate_gif(rz(np.pi / 2), "rz_pi_2", output_dir)
    create_gate_gif(
        H,
        "hadamard_y90_x180",
        output_dir,
        path=[("y", np.pi / 2), ("x", np.pi)],
    )
    create_gate_sequence_gif(
        [
            ("axis", "y", np.pi / 2),
            ("axis", "x", np.pi),
            ("axis", "y", np.pi / 2),
            ("axis", "x", np.pi),
        ],
        "hadamard_then_hadamard",
        output_dir,
    )
    create_gate_sequence_gif(
        [
            ("axis", "y", np.pi / 6),
            ("axis", "y", np.pi / 2),
            ("axis", "x", np.pi),
        ],
        "ry30_then_hadamard",
        output_dir,
    )


if __name__ == "__main__":
    main()
