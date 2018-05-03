# This file was generated by SableCC (http://www.sablecc.org/).
# pylint: disable=too-many-lines,missing-docstring


# pylint: disable=too-many-public-methods
class Analysis(object):
    def __init__(self):
        self._in_ = None
        self._out_ = None

    def get_in(self, node):
        if self._in_ is None:
            return None

        if self._in_ in node:
            return self._in_[node]

        return None

    def set_in(self, node, _in_):
        if self._in_ is None:
            self._in_ = dict()

        if _in_ is not None:
            self._in_[node] = _in_
        else:
            if self._in_ in node:
                del self._in_[node]

    def get_out(self, node):
        if self._out_ is None:
            return None

        if self._out_ in node:
            return self._out_[node]

        return None

    def set_out(self, node, _out_):
        if self._out_ is None:
            self._out_ = dict()

        if _out_ is not None:
            self._out_[node] = _out_
        else:
            if self._out_ in node:
                del self._out_[node]

    def case_start(self, node):
        self.default_case(node)

    def case_alogicstatementstatement(self, node):
        self.default_case(node)

    def case_ascorestatement(self, node):
        self.default_case(node)

    def case_abooleancondition(self, node):
        self.default_case(node)

    def case_astatementcondition(self, node):
        self.default_case(node)

    def case_aresiduecondition(self, node):
        self.default_case(node)

    def case_aexcludecondition(self, node):
        self.default_case(node)

    def case_aselectcondition(self, node):
        self.default_case(node)

    def case_acondition2(self, node):
        self.default_case(node)

    def case_aandlogicsymbol(self, node):
        self.default_case(node)

    def case_aorlogicsymbol(self, node):
        self.default_case(node)

    def case_aresidueresidue(self, node):
        self.default_case(node)

    def case_aresiduenotresidue(self, node):
        self.default_case(node)

    def case_aresidueinvertresidue(self, node):
        self.default_case(node)

    def case_aexcludestatement(self, node):
        self.default_case(node)

    def case_aselectstatement(self, node):
        self.default_case(node)

    def case_aexactlyselectstatement2(self, node):
        self.default_case(node)

    def case_aatleastselectstatement2(self, node):
        self.default_case(node)

    def case_anotmorethanselectstatement2(self, node):
        self.default_case(node)

    def case_aatleastnotmorethanselectstatement2(self, node):
        self.default_case(node)

    def case_aselectlist(self, node):
        self.default_case(node)

    def case_alistitems(self, node):
        self.default_case(node)

    def case_ascorecondition(self, node):
        self.default_case(node)

    def case_ascorelist(self, node):
        self.default_case(node)

    def case_astatementscoreitem(self, node):
        self.default_case(node)

    def case_amaxscoreitem(self, node):
        self.default_case(node)

    def case_ascoreitems(self, node):
        self.default_case(node)

    def case_aintegernumber(self, node):
        self.default_case(node)

    def case_afloatnumber(self, node):
        self.default_case(node)

    def case_tmin(self, node):
        self.default_case(node)

    def case_tand(self, node):
        self.default_case(node)

    def case_tor(self, node):
        self.default_case(node)

    def case_tnot(self, node):
        self.default_case(node)

    def case_texclude(self, node):
        self.default_case(node)

    def case_tselect(self, node):
        self.default_case(node)

    def case_tfrom(self, node):
        self.default_case(node)

    def case_tatleast(self, node):
        self.default_case(node)

    def case_texactly(self, node):
        self.default_case(node)

    def case_tnotmorethan(self, node):
        self.default_case(node)

    def case_tscore(self, node):
        self.default_case(node)

    def case_tmax(self, node):
        self.default_case(node)

    def case_tlpar(self, node):
        self.default_case(node)

    def case_trpar(self, node):
        self.default_case(node)

    def case_tmapper(self, node):
        self.default_case(node)

    def case_tcomma(self, node):
        self.default_case(node)

    def case_tblank(self, node):
        self.default_case(node)

    def case_tinteger(self, node):
        self.default_case(node)

    def case_tfloat(self, node):
        self.default_case(node)

    def case_taminoacid(self, node):
        self.default_case(node)

    def case_eof(self, node):
        self.default_case(node)

    def default_case(self, node):
        pass


# pylint: disable=too-many-public-methods
class DepthFirstAdapter(Analysis):
    def in_start(self, node):
        self.default_in(node)

    def out_start(self, node):
        self.default_out(node)

    def default_in(self, node):
        pass

    def default_out(self, node):
        pass

    def case_start(self, node):
        self.in_start(node)
        node.get_pstatement().apply(self)
        node.get_eof().apply(self)
        self.out_start(node)

    def in_alogicstatementstatement(self, node):
        self.default_in(node)

    def out_alogicstatementstatement(self, node):
        self.default_out(node)

    def case_alogicstatementstatement(self, node):
        self.in_alogicstatementstatement(node)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        self.out_alogicstatementstatement(node)

    def in_ascorestatement(self, node):
        self.default_in(node)

    def out_ascorestatement(self, node):
        self.default_out(node)

    def case_ascorestatement(self, node):
        self.in_ascorestatement(node)
        if node.get_scorecondition() is not None:
            node.get_scorecondition().apply(self)
        self.out_ascorestatement(node)

    def in_abooleancondition(self, node):
        self.default_in(node)

    def out_abooleancondition(self, node):
        self.default_out(node)

    def case_abooleancondition(self, node):
        self.in_abooleancondition(node)
        if node.get_condition() is not None:
            node.get_condition().apply(self)
        temp = node.get_condition2()
        for item in temp:
            item.apply(self)
        self.out_abooleancondition(node)

    def in_astatementcondition(self, node):
        self.default_in(node)

    def out_astatementcondition(self, node):
        self.default_out(node)

    def case_astatementcondition(self, node):
        self.in_astatementcondition(node)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_astatementcondition(node)

    def in_aresiduecondition(self, node):
        self.default_in(node)

    def out_aresiduecondition(self, node):
        self.default_out(node)

    def case_aresiduecondition(self, node):
        self.in_aresiduecondition(node)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        self.out_aresiduecondition(node)

    def in_aexcludecondition(self, node):
        self.default_in(node)

    def out_aexcludecondition(self, node):
        self.default_out(node)

    def case_aexcludecondition(self, node):
        self.in_aexcludecondition(node)
        if node.get_excludestatement() is not None:
            node.get_excludestatement().apply(self)
        self.out_aexcludecondition(node)

    def in_aselectcondition(self, node):
        self.default_in(node)

    def out_aselectcondition(self, node):
        self.default_out(node)

    def case_aselectcondition(self, node):
        self.in_aselectcondition(node)
        if node.get_selectstatement() is not None:
            node.get_selectstatement().apply(self)
        self.out_aselectcondition(node)

    def in_acondition2(self, node):
        self.default_in(node)

    def out_acondition2(self, node):
        self.default_out(node)

    def case_acondition2(self, node):
        self.in_acondition2(node)
        if node.get_logicsymbol() is not None:
            node.get_logicsymbol().apply(self)
        if node.get_condition() is not None:
            node.get_condition().apply(self)
        self.out_acondition2(node)

    def in_aandlogicsymbol(self, node):
        self.default_in(node)

    def out_aandlogicsymbol(self, node):
        self.default_out(node)

    def case_aandlogicsymbol(self, node):
        self.in_aandlogicsymbol(node)
        if node.get_and() is not None:
            node.get_and().apply(self)
        self.out_aandlogicsymbol(node)

    def in_aorlogicsymbol(self, node):
        self.default_in(node)

    def out_aorlogicsymbol(self, node):
        self.default_out(node)

    def case_aorlogicsymbol(self, node):
        self.in_aorlogicsymbol(node)
        if node.get_or() is not None:
            node.get_or().apply(self)
        self.out_aorlogicsymbol(node)

    def in_aresidueresidue(self, node):
        self.default_in(node)

    def out_aresidueresidue(self, node):
        self.default_out(node)

    def case_aresidueresidue(self, node):
        self.in_aresidueresidue(node)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        temp = node.get_mutatedaminoacid()
        for item in temp:
            item.apply(self)
        self.out_aresidueresidue(node)

    def in_aresiduenotresidue(self, node):
        self.default_in(node)

    def out_aresiduenotresidue(self, node):
        self.default_out(node)

    def case_aresiduenotresidue(self, node):
        self.in_aresiduenotresidue(node)
        if node.get_not() is not None:
            node.get_not().apply(self)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        temp = node.get_mutatedaminoacid()
        for item in temp:
            item.apply(self)
        self.out_aresiduenotresidue(node)

    def in_aresidueinvertresidue(self, node):
        self.default_in(node)

    def out_aresidueinvertresidue(self, node):
        self.default_out(node)

    def case_aresidueinvertresidue(self, node):
        self.in_aresidueinvertresidue(node)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_not() is not None:
            node.get_not().apply(self)
        temp = node.get_mutatedaminoacid()
        for item in temp:
            item.apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_aresidueinvertresidue(node)

    def in_aexcludestatement(self, node):
        self.default_in(node)

    def out_aexcludestatement(self, node):
        self.default_out(node)

    def case_aexcludestatement(self, node):
        self.in_aexcludestatement(node)
        if node.get_exclude() is not None:
            node.get_exclude().apply(self)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        self.out_aexcludestatement(node)

    def in_aselectstatement(self, node):
        self.default_in(node)

    def out_aselectstatement(self, node):
        self.default_out(node)

    def case_aselectstatement(self, node):
        self.in_aselectstatement(node)
        if node.get_select() is not None:
            node.get_select().apply(self)
        if node.get_selectstatement2() is not None:
            node.get_selectstatement2().apply(self)
        self.out_aselectstatement(node)

    def in_aexactlyselectstatement2(self, node):
        self.default_in(node)

    def out_aexactlyselectstatement2(self, node):
        self.default_out(node)

    def case_aexactlyselectstatement2(self, node):
        self.in_aexactlyselectstatement2(node)
        if node.get_exactly() is not None:
            node.get_exactly().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_aexactlyselectstatement2(node)

    def in_aatleastselectstatement2(self, node):
        self.default_in(node)

    def out_aatleastselectstatement2(self, node):
        self.default_out(node)

    def case_aatleastselectstatement2(self, node):
        self.in_aatleastselectstatement2(node)
        if node.get_atleast() is not None:
            node.get_atleast().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_aatleastselectstatement2(node)

    def in_anotmorethanselectstatement2(self, node):
        self.default_in(node)

    def out_anotmorethanselectstatement2(self, node):
        self.default_out(node)

    def case_anotmorethanselectstatement2(self, node):
        self.in_anotmorethanselectstatement2(node)
        if node.get_notmorethan() is not None:
            node.get_notmorethan().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_anotmorethanselectstatement2(node)

    def in_aatleastnotmorethanselectstatement2(self, node):
        self.default_in(node)

    def out_aatleastnotmorethanselectstatement2(self, node):
        self.default_out(node)

    def case_aatleastnotmorethanselectstatement2(self, node):
        self.in_aatleastnotmorethanselectstatement2(node)
        if node.get_atleast() is not None:
            node.get_atleast().apply(self)
        if node.get_atleastnumber() is not None:
            node.get_atleastnumber().apply(self)
        if node.get_logicsymbol() is not None:
            node.get_logicsymbol().apply(self)
        if node.get_notmorethan() is not None:
            node.get_notmorethan().apply(self)
        if node.get_notmorethannumber() is not None:
            node.get_notmorethannumber().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_aatleastnotmorethanselectstatement2(node)

    def in_aselectlist(self, node):
        self.default_in(node)

    def out_aselectlist(self, node):
        self.default_out(node)

    def case_aselectlist(self, node):
        self.in_aselectlist(node)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        temp = node.get_listitems()
        for item in temp:
            item.apply(self)
        self.out_aselectlist(node)

    def in_alistitems(self, node):
        self.default_in(node)

    def out_alistitems(self, node):
        self.default_out(node)

    def case_alistitems(self, node):
        self.in_alistitems(node)
        if node.get_comma() is not None:
            node.get_comma().apply(self)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        self.out_alistitems(node)

    def in_ascorecondition(self, node):
        self.default_in(node)

    def out_ascorecondition(self, node):
        self.default_out(node)

    def case_ascorecondition(self, node):
        self.in_ascorecondition(node)
        if node.get_score() is not None:
            node.get_score().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_scorelist() is not None:
            node.get_scorelist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_ascorecondition(node)

    def in_ascorelist(self, node):
        self.default_in(node)

    def out_ascorelist(self, node):
        self.default_out(node)

    def case_ascorelist(self, node):
        self.in_ascorelist(node)
        if node.get_scoreitem() is not None:
            node.get_scoreitem().apply(self)
        temp = node.get_scoreitems()
        for item in temp:
            item.apply(self)
        self.out_ascorelist(node)

    def in_astatementscoreitem(self, node):
        self.default_in(node)

    def out_astatementscoreitem(self, node):
        self.default_out(node)

    def case_astatementscoreitem(self, node):
        self.in_astatementscoreitem(node)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        if node.get_mapper() is not None:
            node.get_mapper().apply(self)
        if node.get_min() is not None:
            node.get_min().apply(self)
        if node.get_number() is not None:
            node.get_number().apply(self)
        self.out_astatementscoreitem(node)

    def in_amaxscoreitem(self, node):
        self.default_in(node)

    def out_amaxscoreitem(self, node):
        self.default_out(node)

    def case_amaxscoreitem(self, node):
        self.in_amaxscoreitem(node)
        if node.get_max() is not None:
            node.get_max().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_scorelist() is not None:
            node.get_scorelist().apply(self)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        self.out_amaxscoreitem(node)

    def in_ascoreitems(self, node):
        self.default_in(node)

    def out_ascoreitems(self, node):
        self.default_out(node)

    def case_ascoreitems(self, node):
        self.in_ascoreitems(node)
        if node.get_comma() is not None:
            node.get_comma().apply(self)
        if node.get_scoreitem() is not None:
            node.get_scoreitem().apply(self)
        self.out_ascoreitems(node)

    def in_aintegernumber(self, node):
        self.default_in(node)

    def out_aintegernumber(self, node):
        self.default_out(node)

    def case_aintegernumber(self, node):
        self.in_aintegernumber(node)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        self.out_aintegernumber(node)

    def in_afloatnumber(self, node):
        self.default_in(node)

    def out_afloatnumber(self, node):
        self.default_out(node)

    def case_afloatnumber(self, node):
        self.in_afloatnumber(node)
        if node.get_float() is not None:
            node.get_float().apply(self)
        self.out_afloatnumber(node)


class ReversedDepthFirstAdapter(Analysis):
    def in_start(self, node):
        self.default_in(node)

    def out_start(self, node):
        self.default_out(node)

    def default_in(self, node):
        pass

    def default_out(self, node):
        pass

    def case_start(self, node):
        self.in_start(node)
        node.get_eof().apply(self)
        node.get_pstatement().apply(self)
        self.out_start(node)

    def in_alogicstatementstatement(self, node):
        self.default_in(node)

    def out_alogicstatementstatement(self, node):
        self.default_out(node)

    def case_alogicstatementstatement(self, node):
        self.in_alogicstatementstatement(node)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        self.out_alogicstatementstatement(node)

    def in_ascorestatement(self, node):
        self.default_in(node)

    def out_ascorestatement(self, node):
        self.default_out(node)

    def case_ascorestatement(self, node):
        self.in_ascorestatement(node)
        if node.get_scorecondition() is not None:
            node.get_scorecondition().apply(self)
        self.out_ascorestatement(node)

    def in_abooleancondition(self, node):
        self.default_in(node)

    def out_abooleancondition(self, node):
        self.default_out(node)

    def case_abooleancondition(self, node):
        self.in_abooleancondition(node)
        temp = node.get_condition2()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_condition() is not None:
            node.get_condition().apply(self)
        self.out_abooleancondition(node)

    def in_astatementcondition(self, node):
        self.default_in(node)

    def out_astatementcondition(self, node):
        self.default_out(node)

    def case_astatementcondition(self, node):
        self.in_astatementcondition(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        self.out_astatementcondition(node)

    def in_aresiduecondition(self, node):
        self.default_in(node)

    def out_aresiduecondition(self, node):
        self.default_out(node)

    def case_aresiduecondition(self, node):
        self.in_aresiduecondition(node)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        self.out_aresiduecondition(node)

    def in_aexcludecondition(self, node):
        self.default_in(node)

    def out_aexcludecondition(self, node):
        self.default_out(node)

    def case_aexcludecondition(self, node):
        self.in_aexcludecondition(node)
        if node.get_excludestatement() is not None:
            node.get_excludestatement().apply(self)
        self.out_aexcludecondition(node)

    def in_aselectcondition(self, node):
        self.default_in(node)

    def out_aselectcondition(self, node):
        self.default_out(node)

    def case_aselectcondition(self, node):
        self.in_aselectcondition(node)
        if node.get_selectstatement() is not None:
            node.get_selectstatement().apply(self)
        self.out_aselectcondition(node)

    def in_acondition2(self, node):
        self.default_in(node)

    def out_acondition2(self, node):
        self.default_out(node)

    def case_acondition2(self, node):
        self.in_acondition2(node)
        if node.get_condition() is not None:
            node.get_condition().apply(self)
        if node.get_logicsymbol() is not None:
            node.get_logicsymbol().apply(self)
        self.out_acondition2(node)

    def in_aandlogicsymbol(self, node):
        self.default_in(node)

    def out_aandlogicsymbol(self, node):
        self.default_out(node)

    def case_aandlogicsymbol(self, node):
        self.in_aandlogicsymbol(node)
        if node.get_and() is not None:
            node.get_and().apply(self)
        self.out_aandlogicsymbol(node)

    def in_aorlogicsymbol(self, node):
        self.default_in(node)

    def out_aorlogicsymbol(self, node):
        self.default_out(node)

    def case_aorlogicsymbol(self, node):
        self.in_aorlogicsymbol(node)
        if node.get_or() is not None:
            node.get_or().apply(self)
        self.out_aorlogicsymbol(node)

    def in_aresidueresidue(self, node):
        self.default_in(node)

    def out_aresidueresidue(self, node):
        self.default_out(node)

    def case_aresidueresidue(self, node):
        self.in_aresidueresidue(node)
        temp = node.get_mutatedaminoacid()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        self.out_aresidueresidue(node)

    def in_aresiduenotresidue(self, node):
        self.default_in(node)

    def out_aresiduenotresidue(self, node):
        self.default_out(node)

    def case_aresiduenotresidue(self, node):
        self.in_aresiduenotresidue(node)
        temp = node.get_mutatedaminoacid()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        if node.get_not() is not None:
            node.get_not().apply(self)
        self.out_aresiduenotresidue(node)

    def in_aresidueinvertresidue(self, node):
        self.default_in(node)

    def out_aresidueinvertresidue(self, node):
        self.default_out(node)

    def case_aresidueinvertresidue(self, node):
        self.in_aresidueinvertresidue(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        temp = node.get_mutatedaminoacid()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_not() is not None:
            node.get_not().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_originalaminoacid() is not None:
            node.get_originalaminoacid().apply(self)
        self.out_aresidueinvertresidue(node)

    def in_aexcludestatement(self, node):
        self.default_in(node)

    def out_aexcludestatement(self, node):
        self.default_out(node)

    def case_aexcludestatement(self, node):
        self.in_aexcludestatement(node)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        if node.get_exclude() is not None:
            node.get_exclude().apply(self)
        self.out_aexcludestatement(node)

    def in_aselectstatement(self, node):
        self.default_in(node)

    def out_aselectstatement(self, node):
        self.default_out(node)

    def case_aselectstatement(self, node):
        self.in_aselectstatement(node)
        if node.get_selectstatement2() is not None:
            node.get_selectstatement2().apply(self)
        if node.get_select() is not None:
            node.get_select().apply(self)
        self.out_aselectstatement(node)

    def in_aexactlyselectstatement2(self, node):
        self.default_in(node)

    def out_aexactlyselectstatement2(self, node):
        self.default_out(node)

    def case_aexactlyselectstatement2(self, node):
        self.in_aexactlyselectstatement2(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_exactly() is not None:
            node.get_exactly().apply(self)
        self.out_aexactlyselectstatement2(node)

    def in_aatleastselectstatement2(self, node):
        self.default_in(node)

    def out_aatleastselectstatement2(self, node):
        self.default_out(node)

    def case_aatleastselectstatement2(self, node):
        self.in_aatleastselectstatement2(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_atleast() is not None:
            node.get_atleast().apply(self)
        self.out_aatleastselectstatement2(node)

    def in_anotmorethanselectstatement2(self, node):
        self.default_in(node)

    def out_anotmorethanselectstatement2(self, node):
        self.default_out(node)

    def case_anotmorethanselectstatement2(self, node):
        self.in_anotmorethanselectstatement2(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        if node.get_notmorethan() is not None:
            node.get_notmorethan().apply(self)
        self.out_anotmorethanselectstatement2(node)

    def in_aatleastnotmorethanselectstatement2(self, node):
        self.default_in(node)

    def out_aatleastnotmorethanselectstatement2(self, node):
        self.default_out(node)

    def case_aatleastnotmorethanselectstatement2(self, node):
        self.in_aatleastnotmorethanselectstatement2(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_selectlist() is not None:
            node.get_selectlist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_notmorethannumber() is not None:
            node.get_notmorethannumber().apply(self)
        if node.get_notmorethan() is not None:
            node.get_notmorethan().apply(self)
        if node.get_logicsymbol() is not None:
            node.get_logicsymbol().apply(self)
        if node.get_atleastnumber() is not None:
            node.get_atleastnumber().apply(self)
        if node.get_atleast() is not None:
            node.get_atleast().apply(self)
        self.out_aatleastnotmorethanselectstatement2(node)

    def in_aselectlist(self, node):
        self.default_in(node)

    def out_aselectlist(self, node):
        self.default_out(node)

    def case_aselectlist(self, node):
        self.in_aselectlist(node)
        temp = node.get_listitems()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        self.out_aselectlist(node)

    def in_alistitems(self, node):
        self.default_in(node)

    def out_alistitems(self, node):
        self.default_out(node)

    def case_alistitems(self, node):
        self.in_alistitems(node)
        if node.get_residue() is not None:
            node.get_residue().apply(self)
        if node.get_comma() is not None:
            node.get_comma().apply(self)
        self.out_alistitems(node)

    def in_ascorecondition(self, node):
        self.default_in(node)

    def out_ascorecondition(self, node):
        self.default_out(node)

    def case_ascorecondition(self, node):
        self.in_ascorecondition(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_scorelist() is not None:
            node.get_scorelist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_from() is not None:
            node.get_from().apply(self)
        if node.get_score() is not None:
            node.get_score().apply(self)
        self.out_ascorecondition(node)

    def in_ascorelist(self, node):
        self.default_in(node)

    def out_ascorelist(self, node):
        self.default_out(node)

    def case_ascorelist(self, node):
        self.in_ascorelist(node)
        temp = node.get_scoreitems()
        temp.reverse()
        for item in temp:
            item.apply(self)
        if node.get_scoreitem() is not None:
            node.get_scoreitem().apply(self)
        self.out_ascorelist(node)

    def in_astatementscoreitem(self, node):
        self.default_in(node)

    def out_astatementscoreitem(self, node):
        self.default_out(node)

    def case_astatementscoreitem(self, node):
        self.in_astatementscoreitem(node)
        if node.get_number() is not None:
            node.get_number().apply(self)
        if node.get_min() is not None:
            node.get_min().apply(self)
        if node.get_mapper() is not None:
            node.get_mapper().apply(self)
        if node.get_booleancondition() is not None:
            node.get_booleancondition().apply(self)
        self.out_astatementscoreitem(node)

    def in_amaxscoreitem(self, node):
        self.default_in(node)

    def out_amaxscoreitem(self, node):
        self.default_out(node)

    def case_amaxscoreitem(self, node):
        self.in_amaxscoreitem(node)
        if node.get_rpar() is not None:
            node.get_rpar().apply(self)
        if node.get_scorelist() is not None:
            node.get_scorelist().apply(self)
        if node.get_lpar() is not None:
            node.get_lpar().apply(self)
        if node.get_max() is not None:
            node.get_max().apply(self)
        self.out_amaxscoreitem(node)

    def in_ascoreitems(self, node):
        self.default_in(node)

    def out_ascoreitems(self, node):
        self.default_out(node)

    def case_ascoreitems(self, node):
        self.in_ascoreitems(node)
        if node.get_scoreitem() is not None:
            node.get_scoreitem().apply(self)
        if node.get_comma() is not None:
            node.get_comma().apply(self)
        self.out_ascoreitems(node)

    def in_aintegernumber(self, node):
        self.default_in(node)

    def out_aintegernumber(self, node):
        self.default_out(node)

    def case_aintegernumber(self, node):
        self.in_aintegernumber(node)
        if node.get_integer() is not None:
            node.get_integer().apply(self)
        self.out_aintegernumber(node)

    def in_afloatnumber(self, node):
        self.default_in(node)

    def out_afloatnumber(self, node):
        self.default_out(node)

    def case_afloatnumber(self, node):
        self.in_afloatnumber(node)
        if node.get_float() is not None:
            node.get_float().apply(self)
        self.out_afloatnumber(node)