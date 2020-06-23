import pytest


@pytest.fixture(scope="class")
def setup():
    print("Running fixture")
    print("Setting up before method run")
    yield
    print("yielding after method run")



@pytest.fixture(params=["Chrome","Firefox"])
def crossBrowser(request):
    return request.param

