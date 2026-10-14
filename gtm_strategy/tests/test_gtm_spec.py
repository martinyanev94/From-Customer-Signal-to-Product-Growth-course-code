from src.gtm_spec import GTMSpec, signaldesk_spec, validate_gtm


def test_signaldesk_spec_is_structurally_complete():
    assert validate_gtm(signaldesk_spec) == []


def test_missing_adoption_measure_is_reported():
    incomplete = GTMSpec(
        product=signaldesk_spec.product,
        target_market=signaldesk_spec.target_market,
        launch_objective=signaldesk_spec.launch_objective,
        journey=signaldesk_spec.journey,
        channels=signaldesk_spec.channels,
        content=signaldesk_spec.content,
        measures=[item for item in signaldesk_spec.measures if item["stage"] != "adopt"],
    )

    assert "launch objective has no adoption measure" in validate_gtm(incomplete)
