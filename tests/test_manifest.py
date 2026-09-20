from agent_site_adapter.manifest import ServiceManifest


def test_manifest_capability_and_profile_match():
    manifest = ServiceManifest(
        service_id="service-1",
        origin="https://service.example",
        protocol_versions=frozenset({"1.0"}),
        profiles=frozenset({"web-http"}),
        capabilities=frozenset({"order"}),
        auth_requirements=frozenset({"oauth"}),
    )
    assert manifest.supports("1.0", "web-http", "order")


def test_manifest_rejects_unknown_profile():
    manifest = ServiceManifest(
        service_id="service-1",
        origin="https://service.example",
        protocol_versions=frozenset({"1.0"}),
        profiles=frozenset({"web-http"}),
        capabilities=frozenset({"order"}),
        auth_requirements=frozenset({"oauth"}),
    )
    assert not manifest.supports("1.0", "other-profile", "order")
