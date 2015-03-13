"""
Copyright 2015 Jason M. Sachs

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

def walk_subsets(items):
    pool = list(items)
    subst = False
    for k in xrange(len(pool)):
        remaining = pool[(k+1):]
        yield pool[k], subst + (k>0), remaining
        # iterating loop can del remaining[:] to stop recursion
        subst = bool(remaining)
        if subst:
            for out in walk_subsets(remaining):
                yield out
