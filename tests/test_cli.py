import subprocess
from pathlib import Path
from utils import compute_image_hash

ASSETS = Path(__file__).parent / "assets"

EXPECTED_CLI_HASHES = {
    "cli_output.png": "<fill-in-later>",
}

def test_cli_runs_and_validates(tmp_path):
    output = tmp_path / "cli_output.png"
    cmd = [
        "python", "-m", "cutstitch.cli",
        str(ASSETS / "img1.png"),
        str(ASSETS / "img2.png"),
        "--mode", "horizontal",
        "--output", str(output),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert output.exists()

    file_hash = compute_image_hash(output)
    if EXPECTED_CLI_HASHES["cli_output.png"] != "<fill-in-later>":
        assert file_hash == EXPECTED_CLI_HASHES["cli_output.png"], f"CLI hash mismatch: {file_hash}"
    else:
        print(f"CLI horizontal hash: {file_hash}")
