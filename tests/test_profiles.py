import pytest

from agent_site_adapter.profiles import (
    V1_PROFILE_AGENT_PAY,
    V1_PROFILE_COMMERCE,
    V1_PROFILE_WEB_HTTP,
    V1_PROFILES,
    ProfileSelection,
    requirements_for,
)


def test_v1_profiles_are_explicit():
    assert V1_PROFILE_WEB_HTTP in V1_PROFILES
    assert V1_PROFILE_COMMERCE in V1_PROFILES
    assert V1_PROFILE_AGENT_PAY in V1_PROFILES


def test_profile_selection_requires_capability_support():
    selection = ProfileSelection(
        protocol_version="1",
        profile=V1_PROFILE_COMMERCE,
        capabilities=frozenset({"checkout", "quote"}),
    )
    assert selection.compatible_with(
        frozenset({V1_PROFILE_COMMERCE}),
        frozenset({"checkout", "quote", "cancel"}),
    )
    assert not selection.compatible_with(
        frozenset({V1_PROFILE_WEB_HTTP}),
        frozenset({"checkout", "quote"}),
    )


def test_unknown_profile_fails_closed():
    with pytest.raises(ValueError):
        requirements_for("site-adapter/unknown/1")
