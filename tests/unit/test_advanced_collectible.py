from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network, AdvancedCollectible
import pytest


def test_can_create_advanced_collectible():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")

    # Act
    STATIC_RNG = 771
    account = get_account()
    advancedCollectible, creationTx = deploy_and_create()
    requestId = creationTx.events["requestedCollectible"]["requestId"]
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, STATIC_RNG, advancedCollectible.address, {"from": account}
    )

    # Assert
    assert advancedCollectible.tokenCounter() == 1
    assert advancedCollectible.tokenIdToClone(0) == STATIC_RNG % 3
