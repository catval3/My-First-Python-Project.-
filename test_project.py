from project import (
validate,
count,
percentages,
find_motif,
get_sequence,
name,
RNA,
translate,
)



def test_validate():

    assert validate("ATCG") is True

    assert validate("AATTGGCC") is True

    assert validate("ATCX") is False


def test_count():

    assert count("AATTGGCC") == (2, 2, 2, 2)


def test_percentages():

    assert percentages("ATCG") == (50.0, 50.0)

    assert percentages("GGCC") == (100.0, 0.0)

    assert percentages("AATT") == (0.0, 100.0)


def test_find_motif():

    assert find_motif("ATGATGCCC", "ATG") == 2

    assert find_motif("ATGATGCCC", "CCC") == 1

    assert find_motif("ATGATGCCC", "GGG") == 0

    assert find_motif("ATGATGCCC", "XYZ") is None


def test_get_sequence():

    assert get_sequence("tp53.fasta").startswith("CTCAAAAGTCTAGAGCC")


def test_name():

    assert name("tp53.fasta") == "TP53"


def test_RNA():

    RNA("ATCG")

    with open("RNAseq.txt", "r") as file:

        assert file.read() == "AUCG"


def test_translate():

    result = translate("ATGGCC", "TEST")

    assert result == ["Met", "Ala"]

    with open("protein_TEST.txt", "r") as file:

        assert file.read() == "Met Ala"