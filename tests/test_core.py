"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_tap_test_class

from tap_ecb.tap import TapECB

# Run standard built-in tap tests from the SDK:
TestTapECB = get_tap_test_class(
    tap_class=TapECB,
    config={},
)
