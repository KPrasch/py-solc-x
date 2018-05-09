from solc import link_code

CODE = "6060604052610199806100126000396000f360606040526000357c01000000000000000000000000000000000000000000000000000000009004806344fd4fa01461004f57806358de5f041461005e578063e7f09e051461006d5761004d565b005b61005c600480505061007c565b005b61006b60048050506100db565b005b61007a600480505061013a565b005b73__TestB_________________________________630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b565b73__TestC_________________________________630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b565b73__TestA_________________________________630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b56"

TEST_A_ADDRESS = "0xd3cda913deb6f67967b99d67acdfa1712c293601"
TEST_B_ADDRESS = "0x304a554a310c7e546dfe434669c62820b7d83490"
TEST_C_ADDRESS = "0xbb9bc244d798123fde783fcc1c72d3bb8c189413"

LINKED_CODE = "6060604052610199806100126000396000f360606040526000357c01000000000000000000000000000000000000000000000000000000009004806344fd4fa01461004f57806358de5f041461005e578063e7f09e051461006d5761004d565b005b61005c600480505061007c565b005b61006b60048050506100db565b005b61007a600480505061013a565b005b73304a554a310c7e546dfe434669c62820b7d83490630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b565b73bb9bc244d798123fde783fcc1c72d3bb8c189413630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b565b73d3cda913deb6f67967b99d67acdfa1712c293601630c55699c604051817c01000000000000000000000000000000000000000000000000000000000281526004018090506000604051808303818660325a03f415610002575050505b56"


def test_partial_code_linking():
    output = link_code(CODE, {'TestA': TEST_A_ADDRESS})
    assert '__TestA__' not in output
    assert '__TestB__' in output
    assert '__TestC__' in output
    assert TEST_A_ADDRESS[2:] in output


def test_full_code_linking():
    output = link_code(CODE, {
        'TestA': TEST_A_ADDRESS,
        'TestB': TEST_B_ADDRESS,
        'TestC': TEST_C_ADDRESS,
    })
    assert '__TestA__' not in output
    assert '__TestB__' not in output
    assert '__TestC__' not in output
    assert TEST_A_ADDRESS[2:] in output
    assert TEST_B_ADDRESS[2:] in output
    assert TEST_C_ADDRESS[2:] in output
    assert output == LINKED_CODE