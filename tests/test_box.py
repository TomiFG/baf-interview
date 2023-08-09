import pytest

from quote_api.models import Box

@pytest.mark.parametrize("box,expected_vol_weight",[
    (Box(count=5,weight_kg=8,lenght=30,width=45,height=65), 14.625),
    (Box(count=0,weight_kg=8,lenght=30,width=45,height=65), 14.625),
    (Box(count=5,weight_kg=0,lenght=0,width=45,height=65), 0)
])
def test_box_volumetric_weight(box, expected_vol_weight) -> None:
    assert box.volumetric_weight == expected_vol_weight

@pytest.mark.parametrize("box,expected_vol_weight",[
    (Box(count=5,weight_kg=8,lenght=30,width=45,height=65), 14.625)
])
def test_box_chargeable_weight(box, expected_vol_weight) -> None:
    assert box.chargable_weight == expected_vol_weight
