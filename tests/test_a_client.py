import pytest

# A client

# reaches out and "get"s a resource from https://foo.bar/api/v1/thing/id
# can "upsert" a changed resource back to https://foo.bar/api/v1/thing/id
# can "upsert" a new resource to https://foo.bar/api/v1/thing/
# uses the requests library to do so

def describe_a_client():
    @pytest.fixture
    def client():
        return Client