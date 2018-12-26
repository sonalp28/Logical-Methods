"""
Provides two functions for handling variable substitution.
Substitutions are represented by dictionaries.
The keys should be Variable objects and the should be
Variables, Constants, and/or Expression objects.
Given a substitution s, the mapping s[v] = t indicates that
every occurrence of v is to be replaced by t.
"""
from expression import *

def substitute(s, e):
    """
    Applies a substitution s to e, returning the result.
    e is a Variable, Constant, or Expression object.
    s is a dictionary mapping Variable keys to
    Variable, Constant, or Expression values.
    The mapping s[v] = t indicates that every occurrence of
    v is to be replaced by t.

    If e is a variable and a key in s, returns s[e].
    Else if e is an expression with operator o and arguments
        ... a_i, ...,
    returns a new expression with operator o, and arguments
        ... substitute(s, a_i), ...
    Else returns e.
    """
    if not isinstance(e, Expression):#e is variable
        for key,value in s.items():
            if key == e:
                return s[e]
    elif isinstance(e, Expression):#e is expression
        op,args = e.operator,e.arguments
        l1 = []
        for arg in args:
            for key,value in s.items():
                if key == arg:
                    l1.append(s[key])
        return Expression(op,l1)
    else:
        return e;

    #raise(Exception("Not yet implemented!"))

def compose(s2, s1):
    """
    Composes two substitutions s2 and s1,
    returning a single equivalent substitution s.
    Applying s is equivalent to applying s1 followed by s2.
    """
    for key, val in s2.items():
        if not isinstance(s2[key],Expression):
            for k,v in s1.items():
                if not isinstance(s1[k],Expression):
                    if s1[k] == key:
                        return {k:s2[key], key:s2[key]}
                    else:
                        return {k:s1[k], key:s2[key]}
                else:
                    op,args = s1[k].operator,s1[k].arguments
                    l1 = []
                    for arg in args:
                        if arg == key:
                            l1.append(s2[key])
                    return {k:Expression(op,l1), key:s2[key]}
        else:
            for k,v in s1.items():
                return {k:s1[k], key:s2[key]}
    #raise(Exception("Not yet implemented!"))

if __name__ == "__main__":

    """
    Some examples of applying and composing substitutions.
    Feel free to edit the following code.
    """

    subs = [
        {"x": "y"},
        {"y": "z"},
        {"x": "P(y)", "y": "P(w)"}]
    subs = [{
        parse_expression(v): parse_expression(e)
        for v, e in s.items()}
        for s in subs]
    print(subs[2])
    s = {"x" : "y"}
    for key,value in s.items():
        print (s[key])
    print(substitute({"x": "A"}, "x"))
    print(substitute(subs[0], parse_expression("P(x)")))

    print(compose(subs[1],subs[0]))
    print(compose(subs[0],subs[1]))
    print(compose(subs[2],subs[0]))
