# AI_Hackathon_Molecular_Dynamics

Frequently in polymer science, the sequence of chemical repeat units plays a large role in material properties. In this project it is desired to predict the lamellar period width, as a function of the sequence of repeat units in the chain. The repeat units may be either of type B or C, encoded in the data as 1 or 0. The complexity of the data increases with increasing value of the interaction parameter between B and C, and thus several data sets with increasing values of the interaction parameter has been provided.

To find a solution to this problem it is desired that you:

1. Develop a model capable of predicting the lamellar period based upon the sequence
2. Determine which members of the sequence, or a collective function of the sequence most influence the lamellar period

Note that one such function in polymer science is $\phi_i$, the fraction of beads of type i.

Enclosed in this directory are four data sets obtained through simulation.

Each data point consists of a 34 dimensional vector, comprised of:

The first entry is the value of the interaction parameter between beads
The second through thirty-third entry are the bead identities starting at the copolymer junction to the end of the chain, encoded as 0 or 1
The final entry is the lamellar period.

All of the data points in sets A, B, and C share a value of the interaction parameter, being 0, 1.0, and 3.5 respectively.
Dataset D however is comprosed of datapoints each with different values of the interaction parameter.
