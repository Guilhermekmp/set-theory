#coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        rho = binary_relation.relation(input_set)
        reflexivel = True
        for i in rho:
            x = i[0]
            if (x,x) not in rho:
                reflexivel = False
        return reflexivel

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
        simetrico = True
        rho = binary_relation.relation(input_set)
        for i in rho:
            x = i[0]
            y = i[1]
            if (y,x) not in rho:
                simetrico = False
        return simetrico

    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        transitivo = True
        rho = binary_relation.relation(input_set)
        for i in rho:
            x = i[0]
            y = i[1]
            for j in rho:
                if(j[0] == y):
                    if(x,j[1]) not in rho:
                        transitivo = False
        return transitivo

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        antisymmetric or False if it is not.
        """
        anti_simetrico = True
        rho = binary_relation.relation(input_set)
        for x,y in rho:
            if (y,x) in rho and x != y:
                anti_simetrico = False
        return anti_simetrico

    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        an equivalence relation or False if it is not.
        """
        utils = BinaryRelationUtils()
        if(utils.verify_symmetry(binary_relation, input_set) and
           utils.verify_transitivity(binary_relation, input_set) and
           utils.verify_reflexivity(binary_relation, input_set)):
            return True
        else:
            return False
    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.

        Note: The partitioning of the set should be a list of subsets.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: [{1, 3, 5, ...}, {2, 4, 6, ...}]) if it is an equivalence relation.
        """
        utils = BinaryRelationUtils()
        lista = []
        if(utils.verify_equivalency(binary_relation, input_set)):
            rho = binary_relation.relation(input_set)
            for x in input_set:
                particionamento = set()
                for y in input_set:
                    if (x,y) in rho:
                        particionamento.add(y)
                if particionamento not in lista:
                    lista.append(particionamento)
            return lista
        else:
            return None
