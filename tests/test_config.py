from config.settings import ENV, BASE_URL

def test_environment_config():
    print(f"\n Environment:{ENV}")
    print(f"\n Base URL : {BASE_URL}")

    assert ENV in ["qa","DEV","staging"]
    assert BASE_URL