class Solution(object):
    def accountsMerge(self, accounts):
        n = len(accounts)
        parents = [x for x in range(n)]
        size = [1 for x in range(n)]

        def find_parent(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def merge(a, b):
            higher = find_parent(a)
            lower = find_parent(b)
            if higher == lower:
                return
            if size[higher] < size[lower]:
                higher, lower = lower, higher
            parents[lower] = higher
            size[higher] += size[lower]
            return

        email_to_index = {}
        
        for index, element in enumerate(accounts):
            for email in element[1:]:
                if email not in email_to_index:
                    email_to_index[email] = index
                else:
                    original_parent = email_to_index[email]
                    curr_parent = index
                    merge(original_parent, curr_parent)
        
        final_hashmap = collections.defaultdict(list)

        for e in email_to_index:
            idx = email_to_index[e]
            par = find_parent(idx)
            final_hashmap[par].append(e)

        result = []
        for parent_index, emails in final_hashmap.items():
            parent_name = accounts[parent_index][0]
            array = [parent_name]
            array.extend(sorted(emails))
            result.append(array)
        return result