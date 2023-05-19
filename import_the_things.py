from foo.bir import main as bir_main
bir_main.whoami()
print(bir_main.__file__)
from foo.bar import main
main.whoami()

import foo
foo.bar.main.whoami()