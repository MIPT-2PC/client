# client
## documentation
TEST
## Run (Linux)

Create venv at first in root directory:
```
python3 -m venv ./venv
```
then activate:

```
source ./venv/bin/activate
```

Now you should prepare [Preprocessor](https://github.com/MIPT-2PC/preprocessor) and run bash scripts:

```
./runClientA.sh
./runClientB.sh
```
There is an opportunity to setup different ports of ClientA (`initiator`) and ClientB, check mentioned scripts
