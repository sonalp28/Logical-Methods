"""
Provides two functions for performing unification.
"""
from expression import *
from substitution import *

def mismatch(e1, e2):
    """
    Finds the first sub-expressions (if any) where e1 and e2 do not match.
    If there are no mismatches, returns (None, None).
    Else, returns (m1, m2), where m1 and m2 are the mismatched sub-expressions.
    e1 and e2 should be Variables, Constants, or Expression objects.
    m1 and m2 should either be both None, or else both
    Variables, Constants, or Expression objects.
    If either e1 or e2 is not an Expression object, and e1 does not equal e2,
    then m1 is e1 and m2 is e2.
    If e1 and e2 are both expressions with different operators,
    or different number of arguments, then m1 is e1 and m2 is e2.
    Else, if ... a1_i ... are the arguments of e1 and ... a2_i ... are the arguments of e2,
    then m1 and m2 should be the first arguments where a1_i does not match a2_i.
    """
    if not(isinstance(e1,Expression)) or not(isinstance(e2,Expression)):
        if e1.__eq__(e2):
            return None,None
        else:
            return e1,e2
    else:
        if e1.__eqOverwritten__(e2):
            op1,argu1 = e1.operator,e1.arguments
            op2,argu2 = e2.operator,e2.arguments
            for i,j in zip(argu1,argu2):
                k,m = mismatch(i,j)
                if k != None and m != None:
                    return k,m
            return None,None

        else:
            return e1,e2
    #raise(Exception("Not yet implemented!"))

def unify(e1, e2):
    """
    Runs the unification algorithm on e1 and e2.
    e1 and e2 should be Variables, Constants, and/or Expression objects.
    You can assume e1 and e2 are already standardized apart.
    If e1 and e2 do not unify, returns False
    Else, returns a substitution s that unifies e1 with e2.
    s is represented as a dictionary.
    The mapping s[v] = t indicates a substitution in which
    every occurrence of v is to be replaced by t.
    """
    s = {}
    flag = False
    l1 = []
    if not isinstance(e1,Expression) and not isinstance(e2,Expression): #both variables/constants
        if isinstance(e1,Constant) and e1 == e2:
            return {}
        elif isinstance(e1,Constant) and e1 != e2:
            return False
        elif isinstance(e1,Variable) and e1 == e2:
            return {}
        elif isinstance(e1,Variable) and e1 != e2:
            return {e1:e2}
    else:
        args1 = e1.arguments
        args2 = e2.arguments
        for x, y in zip(args1,args2):
            if isinstance(x,Expression) and isinstance(y,Expression):
                self.unify(x,y)
            elif isinstance(x,Expression) and not isinstance(y,Expression):
                args = x.arguments
                for arg in args:
                    if isinstance(arg,Constant):
                        flag = True
                if flag:
                    s.update({y:x})
                    l1.append(y)
            elif isinstance(y,Expression) and not isinstance(x,Expression):
                if isinstance(x,Variable):
                    s.update({x:y})
                    l1.append(x)
                else:
                    args = y.arguments
                    for arg in args:
                        if isinstance(arg,Constant):
                            flag = True
                    if flag:
                        s.update({x:y})
                        l1.append(x)
            elif x != y and isinstance(x,Constant):
                    s.update({y:x})
                    l1.append(y)
            elif x != y and isinstance(y,Constant):
                    s.update({x:y})
                    l1.append(x)
        freq = {x:l1.count(x) for x in l1}
        for key in freq:
            if freq[key] > 1:
                return False
        return s

    #raise(Exception("Not yet implemented!"))

if __name__ == "__main__":

    """
    Some examples from the AIMA unification exercises.
    Feel free to edit the following code.
    """
    ep = [
        ("P(A,B,B)", "P(x,y,z)"),
        ("Q(y,G(A,B))", "Q(G(x,x),z)"),
        ("O(F(y),y)", "O(F(x),J)"),
        ("K(F(y),y)", "K(x,x)"),
    ]

    for e1,e2 in ep:
        print(parse_expression(e1), parse_expression(e2))
        print(mismatch(parse_expression(e1), parse_expression(e2)))
        print(unify(parse_expression(e1), parse_expression(e2)))
