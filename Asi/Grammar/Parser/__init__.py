# This file was generated by SableCC (http://www.sablecc.org/).
# pylint: disable=too-many-lines,missing-docstring

from Asi.Grammar.Node import AAndLogicsymbol, AAtleastSelectstatement2, \
                             AAtleastnotmorethanSelectstatement2, \
                             ABooleancondition, ACondition2, \
                             AExactlySelectstatement2, AExcludeCondition, \
                             AExcludestatement, AFloatNumber, \
                             AIntegerNumber, AListitems, \
                             ALogicstatementStatement, AMaxScoreitem, \
                             ANotmorethanSelectstatement2, AOrLogicsymbol, \
                             AResidueCondition, AResidueinvertResidue, \
                             AResiduenotResidue, AResidueResidue, \
                             AScorecondition, AScoreitems, AScorelist, \
                             AScoreStatement, ASelectCondition, \
                             ASelectstatement, ASelectlist, \
                             AStatementCondition, AStatementScoreitem, \
                             Start
from Asi.Grammar.utils import Stack, StringBuffer


class ParserException(Exception):
    def __init__(self, token, value):
        super().__init__()
        self.value = value
        self.token = token

    def get_token(self):
        return self.token

    def __str__(self):
        return self.value


# pylint: disable=too-few-public-methods
class State(object):
    def __init__(self, state, nodes):
        self.state = state
        self.nodes = nodes


# parser actions
ACTION_SHIFT = 0
ACTION_REDUCE = 1
ACTION_ACCEPT = 2
ACTION_ERROR = 3


def new0(self):
    node_list = list()
    node_array_list1 = self.pop()
    pbooleancondition_node2 = node_array_list1[0]
    pstatement_node1 = ALogicstatementStatement(pbooleancondition_node2)
    node_list.append(pstatement_node1)
    return node_list, 0


def new1(self):
    node_list = list()
    node_array_list1 = self.pop()
    pscorecondition_node2 = node_array_list1[0]
    pstatement_node1 = AScoreStatement(pscorecondition_node2)
    node_list.append(pstatement_node1)
    return node_list, 0


def new2(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node3 = list()
    pcondition_node2 = node_array_list1[0]
    pbooleancondition_node1 = ABooleancondition(pcondition_node2, list_node3)
    node_list.append(pbooleancondition_node1)
    return node_list, 1


def new3(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node4 = list()
    pcondition_node2 = node_array_list1[0]
    list_node3 = node_array_list2[0]
    if list_node3 is not None:
        list_node4.extend(list_node3)
    pbooleancondition_node1 = ABooleancondition(pcondition_node2, list_node4)
    node_list.append(pbooleancondition_node1)
    return node_list, 1


def new4(self):
    node_list = list()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tlpar_node2 = node_array_list1[0]
    pbooleancondition_node3 = node_array_list2[0]
    trpar_node4 = node_array_list3[0]
    pcondition_node1 = AStatementCondition(tlpar_node2, pbooleancondition_node3,
                                           trpar_node4)
    node_list.append(pcondition_node1)
    return node_list, 2


def new5(self):
    node_list = list()
    node_array_list1 = self.pop()
    presidue_node2 = node_array_list1[0]
    pcondition_node1 = AResidueCondition(presidue_node2)
    node_list.append(pcondition_node1)
    return node_list, 2


def new6(self):
    node_list = list()
    node_array_list1 = self.pop()
    pexcludestatement_node2 = node_array_list1[0]
    pcondition_node1 = AExcludeCondition(pexcludestatement_node2)
    node_list.append(pcondition_node1)
    return node_list, 2


def new7(self):
    node_list = list()
    node_array_list1 = self.pop()
    pselectstatement_node2 = node_array_list1[0]
    pcondition_node1 = ASelectCondition(pselectstatement_node2)
    node_list.append(pcondition_node1)
    return node_list, 2


def new8(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    plogicsymbol_node2 = node_array_list1[0]
    pcondition_node3 = node_array_list2[0]
    pcondition2_node1 = ACondition2(plogicsymbol_node2, pcondition_node3)
    node_list.append(pcondition2_node1)
    return node_list, 3


def new9(self):
    node_list = list()
    node_array_list1 = self.pop()
    tand_node2 = node_array_list1[0]
    plogicsymbol_node1 = AAndLogicsymbol(tand_node2)
    node_list.append(plogicsymbol_node1)
    return node_list, 4


def new10(self):
    node_list = list()
    node_array_list1 = self.pop()
    tor_node2 = node_array_list1[0]
    plogicsymbol_node1 = AOrLogicsymbol(tor_node2)
    node_list.append(plogicsymbol_node1)
    return node_list, 4


def new11(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node5 = list()
    tinteger_node3 = node_array_list1[0]
    list_node4 = node_array_list2[0]
    if list_node4 is not None:
        list_node5.extend(list_node4)
    presidue_node1 = AResidueResidue(None, tinteger_node3, list_node5)
    node_list.append(presidue_node1)
    return node_list, 5


def new12(self):
    node_list = list()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node5 = list()
    taminoacid_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    list_node4 = node_array_list3[0]
    if list_node4 is not None:
        list_node5.extend(list_node4)
    presidue_node1 = AResidueResidue(taminoacid_node2, tinteger_node3, list_node5)
    node_list.append(presidue_node1)
    return node_list, 5


def new13(self):
    node_list = list()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node6 = list()
    tnot_node2 = node_array_list1[0]
    tinteger_node4 = node_array_list2[0]
    list_node5 = node_array_list3[0]
    if list_node5 is not None:
        list_node6.extend(list_node5)
    presidue_node1 = AResiduenotResidue(tnot_node2, None, tinteger_node4,
                                        list_node6)
    node_list.append(presidue_node1)
    return node_list, 5


def new14(self):
    node_list = list()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node6 = list()
    tnot_node2 = node_array_list1[0]
    taminoacid_node3 = node_array_list2[0]
    tinteger_node4 = node_array_list3[0]
    list_node5 = node_array_list4[0]
    if list_node5 is not None:
        list_node6.extend(list_node5)
    presidue_node1 = AResiduenotResidue(tnot_node2, taminoacid_node3,
                                        tinteger_node4, list_node6)
    node_list.append(presidue_node1)
    return node_list, 5


def new15(self):
    node_list = list()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node7 = list()
    tinteger_node3 = node_array_list1[0]
    tlpar_node4 = node_array_list2[0]
    tnot_node5 = node_array_list3[0]
    list_node6 = node_array_list4[0]
    if list_node6 is not None:
        list_node7.extend(list_node6)
    trpar_node8 = node_array_list5[0]
    presidue_node1 = AResidueinvertResidue(None, tinteger_node3, tlpar_node4,
                                           tnot_node5, list_node7, trpar_node8)
    node_list.append(presidue_node1)
    return node_list, 5


# pylint: disable=too-many-locals
def new16(self):
    node_list = list()
    node_array_list6 = self.pop()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node7 = list()
    taminoacid_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    tlpar_node4 = node_array_list3[0]
    tnot_node5 = node_array_list4[0]
    list_node6 = node_array_list5[0]
    if list_node6 is not None:
        list_node7.extend(list_node6)
    trpar_node8 = node_array_list6[0]
    presidue_node1 = AResidueinvertResidue(taminoacid_node2, tinteger_node3,
                                           tlpar_node4, tnot_node5, list_node7,
                                           trpar_node8)
    node_list.append(presidue_node1)
    return node_list, 5


def new17(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    texclude_node2 = node_array_list1[0]
    presidue_node3 = node_array_list2[0]
    pexcludestatement_node1 = AExcludestatement(texclude_node2, presidue_node3)
    node_list.append(pexcludestatement_node1)
    return node_list, 6


def new18(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tselect_node2 = node_array_list1[0]
    pselectstatement2_node3 = node_array_list2[0]
    pselectstatement_node1 = ASelectstatement(tselect_node2,
                                              pselectstatement2_node3)
    node_list.append(pselectstatement_node1)
    return node_list, 7


def new19(self):
    node_list = list()
    node_array_list6 = self.pop()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    texactly_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    tfrom_node4 = node_array_list3[0]
    tlpar_node5 = node_array_list4[0]
    pselectlist_node6 = node_array_list5[0]
    trpar_node7 = node_array_list6[0]
    pselectstatement2_node1 = AExactlySelectstatement2(texactly_node2,
                                                       tinteger_node3,
                                                       tfrom_node4, tlpar_node5,
                                                       pselectlist_node6,
                                                       trpar_node7)
    node_list.append(pselectstatement2_node1)
    return node_list, 8


def new20(self):
    node_list = list()
    node_array_list6 = self.pop()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tatleast_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    tfrom_node4 = node_array_list3[0]
    tlpar_node5 = node_array_list4[0]
    pselectlist_node6 = node_array_list5[0]
    trpar_node7 = node_array_list6[0]
    pselectstatement2_node1 = AAtleastSelectstatement2(tatleast_node2,
                                                       tinteger_node3,
                                                       tfrom_node4, tlpar_node5,
                                                       pselectlist_node6,
                                                       trpar_node7)
    node_list.append(pselectstatement2_node1)
    return node_list, 8


def new21(self):
    node_list = list()
    node_array_list6 = self.pop()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tnotmorethan_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    tfrom_node4 = node_array_list3[0]
    tlpar_node5 = node_array_list4[0]
    pselectlist_node6 = node_array_list5[0]
    trpar_node7 = node_array_list6[0]
    pselectstatement2_node1 = ANotmorethanSelectstatement2(tnotmorethan_node2,
                                                           tinteger_node3,
                                                           tfrom_node4,
                                                           tlpar_node5,
                                                           pselectlist_node6,
                                                           trpar_node7)
    node_list.append(pselectstatement2_node1)
    return node_list, 8


# pylint: disable=too-many-locals
def new22(self):
    node_list = list()
    node_array_list9 = self.pop()
    node_array_list8 = self.pop()
    node_array_list7 = self.pop()
    node_array_list6 = self.pop()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tatleast_node2 = node_array_list1[0]
    tinteger_node3 = node_array_list2[0]
    plogicsymbol_node4 = node_array_list3[0]
    tnotmorethan_node5 = node_array_list4[0]
    tinteger_node6 = node_array_list5[0]
    tfrom_node7 = node_array_list6[0]
    tlpar_node8 = node_array_list7[0]
    pselectlist_node9 = node_array_list8[0]
    trpar_node10 = node_array_list9[0]
    pselectstatement2_node1 = \
        AAtleastnotmorethanSelectstatement2(tatleast_node2, tinteger_node3,
                                            plogicsymbol_node4,
                                            tnotmorethan_node5,
                                            tinteger_node6, tfrom_node7,
                                            tlpar_node8, pselectlist_node9,
                                            trpar_node10)
    node_list.append(pselectstatement2_node1)
    return node_list, 8


def new23(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node3 = list()
    presidue_node2 = node_array_list1[0]
    pselectlist_node1 = ASelectlist(presidue_node2, list_node3)
    node_list.append(pselectlist_node1)
    return node_list, 9


def new24(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node4 = list()
    presidue_node2 = node_array_list1[0]
    list_node3 = node_array_list2[0]
    if list_node3 is not None:
        list_node4.extend(list_node3)
    pselectlist_node1 = ASelectlist(presidue_node2, list_node4)
    node_list.append(pselectlist_node1)
    return node_list, 9


def new25(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tcomma_node2 = node_array_list1[0]
    presidue_node3 = node_array_list2[0]
    plistitems_node1 = AListitems(tcomma_node2, presidue_node3)
    node_list.append(plistitems_node1)
    return node_list, 10


def new26(self):
    node_list = list()
    node_array_list5 = self.pop()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tscore_node2 = node_array_list1[0]
    tfrom_node3 = node_array_list2[0]
    tlpar_node4 = node_array_list3[0]
    pscorelist_node5 = node_array_list4[0]
    trpar_node6 = node_array_list5[0]
    pscorecondition_node1 = AScorecondition(tscore_node2, tfrom_node3,
                                            tlpar_node4, pscorelist_node5,
                                            trpar_node6)
    node_list.append(pscorecondition_node1)
    return node_list, 11


def new27(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node3 = list()
    pscoreitem_node2 = node_array_list1[0]
    pscorelist_node1 = AScorelist(pscoreitem_node2, list_node3)
    node_list.append(pscorelist_node1)
    return node_list, 12


def new28(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node4 = list()
    pscoreitem_node2 = node_array_list1[0]
    list_node3 = node_array_list2[0]
    if list_node3 is not None:
        list_node4.extend(list_node3)
    pscorelist_node1 = AScorelist(pscoreitem_node2, list_node4)
    node_list.append(pscorelist_node1)
    return node_list, 12


def new29(self):
    node_list = list()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    pbooleancondition_node2 = node_array_list1[0]
    tmapper_node3 = node_array_list2[0]
    pnumber_node5 = node_array_list3[0]
    pscoreitem_node1 = AStatementScoreitem(pbooleancondition_node2,
                                           tmapper_node3, None,
                                           pnumber_node5)
    node_list.append(pscoreitem_node1)
    return node_list, 13


def new30(self):
    node_list = list()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    pbooleancondition_node2 = node_array_list1[0]
    tmapper_node3 = node_array_list2[0]
    tmin_node4 = node_array_list3[0]
    pnumber_node5 = node_array_list4[0]
    pscoreitem_node1 = AStatementScoreitem(pbooleancondition_node2,
                                           tmapper_node3, tmin_node4,
                                           pnumber_node5)
    node_list.append(pscoreitem_node1)
    return node_list, 13


def new31(self):
    node_list = list()
    node_array_list4 = self.pop()
    node_array_list3 = self.pop()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tmax_node2 = node_array_list1[0]
    tlpar_node3 = node_array_list2[0]
    pscorelist_node4 = node_array_list3[0]
    trpar_node5 = node_array_list4[0]
    pscoreitem_node1 = AMaxScoreitem(tmax_node2, tlpar_node3, pscorelist_node4,
                                     trpar_node5)
    node_list.append(pscoreitem_node1)
    return node_list, 13


def new32(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    tcomma_node2 = node_array_list1[0]
    pscoreitem_node3 = node_array_list2[0]
    pscoreitems_node1 = AScoreitems(tcomma_node2, pscoreitem_node3)
    node_list.append(pscoreitems_node1)
    return node_list, 14


def new33(self):
    node_list = list()
    node_array_list1 = self.pop()
    tinteger_node2 = node_array_list1[0]
    pnumber_node1 = AIntegerNumber(tinteger_node2)
    node_list.append(pnumber_node1)
    return node_list, 15


def new34(self):
    node_list = list()
    node_array_list1 = self.pop()
    tfloat_node2 = node_array_list1[0]
    pnumber_node1 = AFloatNumber(tfloat_node2)
    node_list.append(pnumber_node1)
    return node_list, 15


def new35(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node2 = list()
    pcondition2_node1 = node_array_list1[0]
    if pcondition2_node1 is not None:
        list_node2.append(pcondition2_node1)
    node_list.append(list_node2)
    return node_list, 16


def new36(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node3 = list()
    list_node1 = node_array_list1[0]
    pcondition2_node2 = node_array_list2[0]
    if list_node1 is not None:
        list_node3.extend(list_node1)
    if pcondition2_node2 is not None:
        list_node3.append(pcondition2_node2)
    node_list.append(list_node3)
    return node_list, 16


def new37(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node2 = list()
    taminoacid_node1 = node_array_list1[0]
    if taminoacid_node1 is not None:
        list_node2.append(taminoacid_node1)
    node_list.append(list_node2)
    return node_list, 17


def new38(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node3 = list()
    list_node1 = node_array_list1[0]
    taminoacid_node2 = node_array_list2[0]
    if list_node1 is not None:
        list_node3.extend(list_node1)
    if taminoacid_node2 is not None:
        list_node3.append(taminoacid_node2)
    node_list.append(list_node3)
    return node_list, 17


def new39(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node2 = list()
    plistitems_node1 = node_array_list1[0]
    if plistitems_node1 is not None:
        list_node2.append(plistitems_node1)
    node_list.append(list_node2)
    return node_list, 18


def new40(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node3 = list()
    list_node1 = node_array_list1[0]
    plistitems_node2 = node_array_list2[0]
    if list_node1 is not None:
        list_node3.extend(list_node1)
    if plistitems_node2 is not None:
        list_node3.append(plistitems_node2)
    node_list.append(list_node3)
    return node_list, 18


def new41(self):
    node_list = list()
    node_array_list1 = self.pop()
    list_node2 = list()
    pscoreitems_node1 = node_array_list1[0]
    if pscoreitems_node1 is not None:
        list_node2.append(pscoreitems_node1)
    node_list.append(list_node2)
    return node_list, 19


def new42(self):
    node_list = list()
    node_array_list2 = self.pop()
    node_array_list1 = self.pop()
    list_node3 = list()
    list_node1 = node_array_list1[0]
    pscoreitems_node2 = node_array_list2[0]
    if list_node1 is not None:
        list_node3.extend(list_node1)
    if pscoreitems_node2 is not None:
        list_node3.append(pscoreitems_node2)
    node_list.append(list_node3)
    return node_list, 19


NEWNODE = [
    new0,
    new1,
    new2,
    new3,
    new4,
    new5,
    new6,
    new7,
    new8,
    new9,
    new10,
    new11,
    new12,
    new13,
    new14,
    new15,
    new16,
    new17,
    new18,
    new19,
    new20,
    new21,
    new22,
    new23,
    new24,
    new25,
    new26,
    new27,
    new28,
    new29,
    new30,
    new31,
    new32,
    new33,
    new34,
    new35,
    new36,
    new37,
    new38,
    new39,
    new40,
    new41,
    new42
]

ACTION_TABLE = [
    [
        [-1, 3, 0],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [10, 0, 4],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 1],
        [16, 0, 15],
        [18, 0, 16],
    ],
    [
        [-1, 3, 2],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 3],
        [7, 0, 18],
        [8, 0, 19],
        [9, 0, 20],
    ],
    [
        [-1, 3, 4],
        [6, 0, 22],
    ],
    [
        [-1, 3, 5],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 6],
        [12, 0, 24],
        [18, 0, 25],
    ],
    [
        [-1, 3, 7],
        [16, 0, 27],
    ],
    [
        [-1, 3, 8],
        [19, 2, -1],
    ],
    [
        [-1, 1, 0],
    ],
    [
        [-1, 1, 2],
        [1, 0, 28],
        [2, 0, 29],
    ],
    [
        [-1, 1, 5],
    ],
    [
        [-1, 1, 6],
    ],
    [
        [-1, 1, 7],
    ],
    [
        [-1, 1, 1],
    ],
    [
        [-1, 3, 15],
        [18, 0, 25],
    ],
    [
        [-1, 3, 16],
        [16, 0, 34],
    ],
    [
        [-1, 1, 17],
    ],
    [
        [-1, 3, 18],
        [16, 0, 35],
    ],
    [
        [-1, 3, 19],
        [16, 0, 36],
    ],
    [
        [-1, 3, 20],
        [16, 0, 37],
    ],
    [
        [-1, 1, 18],
    ],
    [
        [-1, 3, 22],
        [12, 0, 38],
    ],
    [
        [-1, 3, 23],
        [13, 0, 39],
    ],
    [
        [-1, 3, 24],
        [3, 0, 40],
    ],
    [
        [-1, 1, 37],
    ],
    [
        [-1, 1, 11],
        [18, 0, 41],
    ],
    [
        [-1, 3, 27],
        [12, 0, 42],
        [18, 0, 25],
    ],
    [
        [-1, 1, 9],
    ],
    [
        [-1, 1, 10],
    ],
    [
        [-1, 1, 35],
    ],
    [
        [-1, 3, 31],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 1, 3],
        [1, 0, 28],
        [2, 0, 29],
    ],
    [
        [-1, 1, 13],
        [18, 0, 41],
    ],
    [
        [-1, 3, 34],
        [18, 0, 25],
    ],
    [
        [-1, 3, 35],
        [1, 0, 28],
        [2, 0, 29],
        [6, 0, 47],
    ],
    [
        [-1, 3, 36],
        [6, 0, 49],
    ],
    [
        [-1, 3, 37],
        [6, 0, 50],
    ],
    [
        [-1, 3, 38],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [11, 0, 51],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 1, 4],
    ],
    [
        [-1, 3, 40],
        [18, 0, 25],
    ],
    [
        [-1, 1, 38],
    ],
    [
        [-1, 3, 42],
        [3, 0, 56],
    ],
    [
        [-1, 1, 12],
        [18, 0, 41],
    ],
    [
        [-1, 1, 8],
    ],
    [
        [-1, 1, 36],
    ],
    [
        [-1, 1, 14],
        [18, 0, 41],
    ],
    [
        [-1, 3, 47],
        [12, 0, 57],
    ],
    [
        [-1, 3, 48],
        [9, 0, 58],
    ],
    [
        [-1, 3, 49],
        [12, 0, 59],
    ],
    [
        [-1, 3, 50],
        [12, 0, 60],
    ],
    [
        [-1, 3, 51],
        [12, 0, 61],
    ],
    [
        [-1, 3, 52],
        [14, 0, 62],
    ],
    [
        [-1, 3, 53],
        [13, 0, 63],
    ],
    [
        [-1, 1, 27],
        [15, 0, 64],
    ],
    [
        [-1, 3, 55],
        [13, 0, 67],
        [18, 0, 41],
    ],
    [
        [-1, 3, 56],
        [18, 0, 25],
    ],
    [
        [-1, 3, 57],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 58],
        [16, 0, 71],
    ],
    [
        [-1, 3, 59],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 60],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 61],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [11, 0, 51],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 62],
        [0, 0, 75],
        [16, 0, 76],
        [17, 0, 77],
    ],
    [
        [-1, 1, 26],
    ],
    [
        [-1, 3, 64],
        [3, 0, 1],
        [4, 0, 2],
        [5, 0, 3],
        [11, 0, 51],
        [12, 0, 5],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 1, 41],
    ],
    [
        [-1, 1, 28],
        [15, 0, 64],
    ],
    [
        [-1, 1, 15],
    ],
    [
        [-1, 3, 68],
        [13, 0, 81],
        [18, 0, 41],
    ],
    [
        [-1, 1, 23],
        [15, 0, 82],
    ],
    [
        [-1, 3, 70],
        [13, 0, 85],
    ],
    [
        [-1, 3, 71],
        [6, 0, 86],
    ],
    [
        [-1, 3, 72],
        [13, 0, 87],
    ],
    [
        [-1, 3, 73],
        [13, 0, 88],
    ],
    [
        [-1, 3, 74],
        [13, 0, 89],
    ],
    [
        [-1, 3, 75],
        [16, 0, 76],
        [17, 0, 77],
    ],
    [
        [-1, 1, 33],
    ],
    [
        [-1, 1, 34],
    ],
    [
        [-1, 1, 29],
    ],
    [
        [-1, 1, 32],
    ],
    [
        [-1, 1, 42],
    ],
    [
        [-1, 1, 16],
    ],
    [
        [-1, 3, 82],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 1, 39],
    ],
    [
        [-1, 1, 24],
        [15, 0, 82],
    ],
    [
        [-1, 1, 20],
    ],
    [
        [-1, 3, 86],
        [12, 0, 93],
    ],
    [
        [-1, 1, 19],
    ],
    [
        [-1, 1, 21],
    ],
    [
        [-1, 1, 31],
    ],
    [
        [-1, 1, 30],
    ],
    [
        [-1, 1, 25],
    ],
    [
        [-1, 1, 40],
    ],
    [
        [-1, 3, 93],
        [3, 0, 1],
        [16, 0, 6],
        [18, 0, 7],
    ],
    [
        [-1, 3, 94],
        [13, 0, 95],
    ],
    [
        [-1, 1, 22],
    ],
]

PARSER_GO_TO_TABLE = [
    [
        [-1, 8],
    ],
    [
        [-1, 52],
        [0, 9],
        [5, 23],
    ],
    [
        [-1, 10],
        [31, 44],
    ],
    [
        [-1, 30],
        [32, 45],
    ],
    [
        [-1, 31],
        [35, 48],
    ],
    [
        [-1, 11],
        [2, 17],
        [57, 69],
        [59, 69],
        [60, 69],
        [82, 91],
        [93, 69],
    ],
    [
        [-1, 12],
    ],
    [
        [-1, 13],
    ],
    [
        [-1, 21],
    ],
    [
        [-1, 70],
        [59, 72],
        [60, 73],
        [93, 94],
    ],
    [
        [-1, 83],
        [84, 92],
    ],
    [
        [-1, 14],
    ],
    [
        [-1, 53],
        [61, 74],
    ],
    [
        [-1, 54],
        [64, 79],
    ],
    [
        [-1, 65],
        [66, 80],
    ],
    [
        [-1, 78],
        [75, 90],
    ],
    [
        [-1, 32],
    ],
    [
        [-1, 26],
        [15, 33],
        [27, 43],
        [34, 46],
        [40, 55],
        [56, 68],
    ],
    [
        [-1, 84],
    ],
    [
        [-1, 66],
    ],
]

ERROR_MESSAGES = \
    [
        "expecting: 'NOT', 'EXCLUDE', 'SELECT', 'SCORE', '(', integer, amino acid",
        "expecting: integer, amino acid",
        "expecting: 'NOT', integer, amino acid",
        "expecting: 'ATLEAST', 'EXACTLY', 'NOTMORETHAN'",
        "expecting: 'FROM'",
        "expecting: 'NOT', 'EXCLUDE', 'SELECT', '(', integer, amino acid",
        "expecting: '(', amino acid",
        "expecting: integer",
        "expecting: EOF",
        "expecting: 'AND', 'OR', ')', '=>', EOF",
        "expecting: amino acid",
        "expecting: '('",
        "expecting: ')'",
        "expecting: 'NOT'",
        "expecting: 'AND', 'OR', ')', '=>', ', ', amino acid, EOF",
        "expecting: 'NOT', 'EXCLUDE', 'SELECT', 'NOTMORETHAN', '(', integer, amino acid",
        "expecting: 'AND', 'OR', 'FROM'",
        "expecting: 'NOT', 'EXCLUDE', 'SELECT', 'MAX', '(', integer, amino acid",
        "expecting: 'NOTMORETHAN'",
        "expecting: '=>'",
        "expecting: ')', ', '",
        "expecting: ')', amino acid",
        "expecting: '-', integer, float",
        "expecting: 'AND', 'OR', ')', '=>', ', ', EOF",
        "expecting: integer, float",
    ]

ERRORS = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9, 8, 10, 7, 9, 7, 7, 7, 9,
    11, 12, 13, 14, 14, 6, 15, 15, 9, 5, 9, 14, 10, 16, 4, 4, 17, 9,
    10, 14, 13, 14, 9, 9, 14, 11, 18, 11, 11, 11, 19, 12, 20, 21, 10,
    2, 7, 2, 2, 17, 22, 8, 17, 20, 20, 23, 21, 20, 12, 4, 12, 12, 12,
    24, 20, 20, 20, 20, 20, 23, 2, 20, 20, 9, 11, 9, 9, 20, 20, 20, 20,
    2, 12, 9,
]


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.stack = Stack()

    def go_to(self, index):
        state = self.state()
        low = 1
        high = len(PARSER_GO_TO_TABLE[index]) - 1
        value = PARSER_GO_TO_TABLE[index][0][1]

        while low <= high:
            middle = (int)((low + high) / 2)

            if state < PARSER_GO_TO_TABLE[index][middle][0]:
                high = middle - 1
            elif state > PARSER_GO_TO_TABLE[index][middle][0]:
                low = middle + 1
            else:
                value = PARSER_GO_TO_TABLE[index][middle][1]
                break

        return value

    def push(self, numstate, list_node):
        self.stack.push(State(numstate, list_node))

    def state(self):
        return self.stack.peek().state

    def pop(self):
        return self.stack.pop().nodes

    def parse(self):
        self.push(0, None)
        lexer = self.lexer
        last_pos = 0
        last_line = 0
        last_token = None
        action = [0, 0]

        while 1:
            while lexer.peek().TokenIndex == -1:
                lexer.next()

            token = lexer.peek()
            last_pos = token.get_pos()
            last_line = token.get_line()
            last_token = token

            index = token.TokenIndex
            action[0] = ACTION_TABLE[self.state()][0][1]
            action[1] = ACTION_TABLE[self.state()][0][2]

            low = 1
            high = len(ACTION_TABLE[self.state()]) - 1

            while low <= high:
                middle = (int)((low + high) / 2)

                if index < ACTION_TABLE[self.state()][middle][0]:
                    high = middle - 1
                elif index > ACTION_TABLE[self.state()][middle][0]:
                    low = middle + 1
                else:
                    action[0] = ACTION_TABLE[self.state()][middle][1]
                    action[1] = ACTION_TABLE[self.state()][middle][2]
                    break

            if action[0] == ACTION_SHIFT:
                node_list = list()
                node_list.append(lexer.next())
                self.push(action[1], node_list)
            elif action[0] == ACTION_REDUCE:
                if action[1] >= 0 and action[1] <= 42:
                    node_list, leftside = NEWNODE[action[1]](self)
                    self.push(self.go_to(leftside), node_list)
            elif action[0] == ACTION_ACCEPT:
                node2 = lexer.next()
                node1 = self.pop()[0]
                return Start(node1, node2)
            elif action[0] == ACTION_ERROR:
                raise ParserException(last_token, "[" + str(last_line) + ","
                                      + str(last_pos) + "] "
                                      + ERROR_MESSAGES[ERRORS[action[1]]])

    @classmethod
    def unescape(cls, string):
        _out_ = StringBuffer()

        for i, char in enumerate(string):
            if char == '\\' and (i + 1) < len(string):
                i += 1
                if string[i] in ['n', 'r', '"', '\\']:
                    _out_.append(
                        {
                            'n': "\n",
                            'r': "\r",
                            '"': '\"',
                            '\\': "\\"
                        }[string[i]]
                    )
                elif string[i] == '0':
                    if string[i:].startswith("000"):
                        _out_.append("\000")
                        i += 2
                    else:
                        _out_.append("\\")
                        _out_.append(string[i])
                elif string[i] == 'u':
                    hstr = string[i+1:(i + 5)]

                    if len(hstr) == 4:
                        try:
                            _out_.append(chr(int(hstr, 16)))
                            i += 5
                        except ValueError:
                            _out_.append("\\")
                            _out_.append(string[i])
                    else:
                        _out_.append("\\")
                        _out_.append(string[i])
                else:
                    _out_.append("\\")
                    _out_.append(string[i])
            else:
                _out_.append(char)

        return str(_out_)