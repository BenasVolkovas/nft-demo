from scripts.helpful_scripts import (
    get_account,
    get_contract,
    fund_with_link,
    OPENSEA_URL,
)
from brownie import AdvancedCollectible, config, network


def deploy_and_create():
    account = get_account()
    advancedCollectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    fund_with_link(advancedCollectible.address)
    creatingTx = advancedCollectible.createCollectible({"from": account})
    creatingTx.wait(1)
    print(f"New collectible created")


def main():
    deploy_and_create()
