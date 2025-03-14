"""Unit Tests."""

from molecule import api


def test_container_driver_is_detected():
    """Check that driver is recognized."""
    assert "lxd" in [str(d) for d in api.drivers()]
