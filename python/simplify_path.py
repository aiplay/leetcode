#!/usr/bin/env python
# encoding: utf-8

# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        temp = list()
        for item in path_list:
            if item == '.' or item == '':
                continue
            elif item == '..':
                if len(temp) > 0:
                    temp.pop()
            else:
                temp.append('/'+item)
        new_path = ''.join(temp)
        if new_path == '':
            new_path = '/'
        print new_path
        return new_path


if __name__ == '__main__':
    # path = '/Users/xujh/android/./../sdk/'
    path = '/'
    solution = Solution()
    solution.simplifyPath(path)
