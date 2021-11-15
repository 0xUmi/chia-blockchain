import json
from typing import Any, Optional, Dict
from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.util.byte_types import hexstr_to_bytes


async def create_kv_store_cmd(wallet_client: WalletRpcClient) -> Optional[Dict[str, Any]]:
    # TODO: nice cli error handling
    try:
        response = await wallet_client.create_kv_store()
    except Exception as e:
        print(f"Exception from 'data': {e}")
        return None
    return response


async def get_value_cmd(args: dict, wallet_client: WalletRpcClient) -> Optional[Dict[str, Any]]:
    # TODO: nice cli error handling
    tree_id = args.get("tree_id", None)
    key = args.get("key", None)
    tree_id_bytes = bytes32(hexstr_to_bytes(tree_id))
    key_bytes = hexstr_to_bytes(key)
    try:
        response = await wallet_client.get_value(tree_id=tree_id_bytes, key=key_bytes)
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Exception from 'data': {e}")
        return None
    return response


async def update_kv_store_cmd(args: dict, wallet_client: WalletRpcClient) -> Optional[Dict[str, Any]]:
    # TODO: nice cli error handling
    tree_id = args.get("tree_id", None)
    changelist = args.get("changelist", None)
    tree_id_bytes = bytes32(hexstr_to_bytes(tree_id))
    try:
        response = await wallet_client.update_kv_store(tree_id=tree_id_bytes, changelist=changelist)
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Exception from 'data': {e}")
        return None
    return response
