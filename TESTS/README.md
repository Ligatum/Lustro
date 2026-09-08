Agregate test results performed on the Lustro_Audit code. Test source files are included in this folder.<br>

Please note that BigCrush, PractRand, NIST and SMHasher are performed using dedicated test wrappers designed specifically to stress the raw Lustro Core state. These wrappers are not production implementations and exist solely to evaluate the statistical behavior of the underlying mechanism.<br>

NIST source files are omitted due to their large size. These may be included on a later date, if required. I am investigating on why the parser is flagging 203 values. It's a tiny fraction overall in the grand total of calculations. However, once I locate the root cause I will update the results accordingly.<br>

Practrand tests will be updated in the future to include longer runs.<br>
