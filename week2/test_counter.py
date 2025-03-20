import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_and_gate(dut):
    """Test cổng AND"""
    
    # Set input = 0 & 0, rồi đợi 10ns
    dut.a.value = 0
    dut.b.value = 0
    await Timer(10, units="ns")
    assert dut.y.value == 0, f"AND(0,0) failed! Got {dut.y.value}"

    # Test 0 & 1
    dut.a.value = 0
    dut.b.value = 1
    await Timer(10, units="ns")
    assert dut.y.value == 0, f"AND(0,1) failed! Got {dut.y.value}"

    # Test 1 & 0
    dut.a.value = 1
    dut.b.value = 0
    await Timer(10, units="ns")
    assert dut.y.value == 0, f"AND(1,0) failed! Got {dut.y.value}"

    # Test 1 & 1
    dut.a.value = 1
    dut.b.value = 1
    await Timer(10, units="ns")
    assert dut.y.value == 1, f"AND(1,1) failed! Got {dut.y.value}"

    cocotb.log.info("Tất cả test đều PASS!")
