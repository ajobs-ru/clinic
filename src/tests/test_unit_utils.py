from utils import helpers


class TestHelpers:
    def test_password_length(self):
        result = helpers.password(length=12)
        assert len(result) == 12

    def test_auto_cast_none_values(self):
        assert helpers.auto_cast("none") is None
        assert helpers.auto_cast("None") is None
        assert helpers.auto_cast("NONE") is None
        assert helpers.auto_cast("null") is None
        assert helpers.auto_cast("NULL") is None
        assert helpers.auto_cast("  none  ") is None
