Which model performed worst and why might you have expected that model to have performed worst?

Bigram model preformed the worse! No values were recorded because word combinations had not been encountered. This caused major issues when trying to parse for perplexity. The corpus did not know how to handle issues.

Did smoothing help or hurt the model’s ‘performance’ when evaluated on this corpus? Why might that be?

Smoothing greatly enhanced the performance of the n-gram. Values that could not previously be determined had a value to go off of. This solved all the 0 issue that was encountered.

For clarification, commands used:
  python programN.py doyle-27.txt doyle-case-27.txt > output.txt
