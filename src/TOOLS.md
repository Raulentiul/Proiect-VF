# Tools

## DeepMIP

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6982973
- **Status:** Unknown
- **Last updated:** 2022-08-15T02:27:01.428268+00:00

### Description
Code for DeepMIP and MiniMIP algorithms.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Dataset: Feedforward Neural Network Verification in Isabelle/HOL

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7427122
- **Status:** Unknown
- **Last updated:** 2024-07-15T14:39:53.754857+00:00

### Description
This data set complements the publication


	  A.D. Brucker and A. Stell. Verifying feedforward neural networks for classification in  Isabelle/HOL. In M. Chechik, J.-P. Katoen, and M. Leucker, editors, Formal Methods (FM 2023). Lübeck, Germany, 2023. ISBN: 978-3-642-38915-3.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## On Applying Residual Reasoning within Neural Network Verification

- **Website:** N/A
- **DOI:** 10.5281/zenodo.8224307
- **Status:** Unknown
- **Last updated:** 2023-08-27T14:26:50.246391+00:00

### Description
As neural networks are increasingly being integrated into mission-critical systems, it is becoming crucial to ensure that they meet
various safety and liveness requirements. Towards, that end, numerous complete and sound verification techniques have been proposed in recent years, but these often suffer from severe scalability issues. One recently proposed approach for improving the scalability of verification techniques is to enhance them with abstraction-refinement capabilities: instead of verifying a complex and large network, abstraction allows the verifier to construct and then verify a much smaller network; and the correctness of the smaller network immediately implies the correctness of the original, larger network. One shortcoming of this scheme is that whenever the
smaller network cannot be verified, the verifier must perform a refinement step, in which the size of the network being verified is increased. The verifier then starts verifying the new network from scratch — effectively “forgetting” its earlier work, in which the  smaller network was verified. Here, we present an enhancement to abstraction-based neural network verification, which uses residual reasoning: a process where information acquired when verifying an abstract network is utilized in order to facilitate the verification of refined networks. At its core, the method enables the verifier to retain information about parts of the search space
in which it was determined that the refined network behaves correctly, allowing the verifier to focus on areas of the search space where bugs might yet be discovered. For evaluation, we implemented our approach as an extension to the Marabou verifier, and obtained highly promising results.

### Used for
- safety
- liveness

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- liveness

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for DNNV: A Framework for Deep Neural Network Verification

- **Website:** N/A
- **DOI:** 10.5281/zenodo.4883626
- **Status:** Unknown
- **Last updated:** 2021-06-01T01:48:10.582750+00:00

### Description
Despite the large number of sophisticated deep neural network (DNN) verification algorithms, DNN verifier developers, users, and researchers still face several challenges. First, verifier developers must contend with the rapidly changing DNN field to support new DNN operations and property types. Second, verifier users have the burden of selecting a verifier input format to specify their problem. Due to the many input formats, this decision can greatly restrict the verifiers that a user may run. Finally, researchers face difficulties in re-using benchmarks to evaluate and compare verifiers, due to the large number of input formats required to run different verifiers. Existing benchmarks are rarely in formats supported by verifiers other than the one for which the benchmark was introduced. In this work we present DNNV, a framework for reducing the burden on DNN verifier researchers, developers, and users. DNNV standardizes input and output formats, includes a simple yet expressive DSL for specifying DNN properties, and provides powerful simplification and reduction operations to facilitate the application, development, and comparison of DNN verifiers. We show how DNNV increases the support of verifiers for existing benchmarks from 30% to 74%.

We provide an artifact containing the DNNV tool for DNN verification, as well as some benchmark problems on which to run DNNV. The artifact is provided as a virtual machine running Ubuntu 20.04, and is functional, available, and re-usable. The artifact for evaluation is made permanently available at https://doi.org/10.5281/zenodo.4717923, with the tool source code and documentation made available for re-use at https://github.com/dlshriver/DNNV and https://dnnv.readthedocs.io, respectively.

### Used for
(none)

### Input formats
- ONNX

### Supported languages
(none)

### Supported inputs
- ONNX

### Properties verified
(none)

### Techniques
- neural network verification techniques
- SMT solving

### External tools
- TensorFlow

### Examples
(none)

### References
(none)


---

## Artifact: Example Guided Synthesis of Linear Approximations for Neural Network Verification

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6525186
- **Status:** Unknown
- **Last updated:** 2022-05-07T01:49:23.189138+00:00

### Description
This is the artifact for the paper "Example Guided Synthesis of Linear Approximations for Neural Network Verification" published at CAV 2022. The zip file contains a Readme.txt explaining how to use the artifact, and reproduce our results.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
- neural network verification techniques

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact of GenBaB: Neural Network Verification with Branch-and-Bound for General Nonlinearities

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14745058
- **Status:** Unknown
- **Last updated:** 2025-01-27T08:19:03.920766+00:00

### Description
(none)

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## TACAS'25 Artifact Submission: The NeuralSAT DPLL(T) Framework For Deep Neural Network Verification

- **Website:** N/A
- **DOI:** 10.5281/zenodo.13985134
- **Status:** Unknown
- **Last updated:** 2024-10-24T12:37:08.923583+00:00

### Description
(none)

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Building Verified Neural Networks for Computer Systems with Ouroboros

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7788500
- **Status:** Unknown
- **Last updated:** 2023-03-31T14:26:38.112069+00:00

### Description
Neural networks are powerful tools. Applying them in computer systems—operating systems, databases, and networked systems—attracts much attention. However, neural networks are complicated black boxes that may produce unexpected results. To train networks with well-defined behaviors, we introduce ouroboros, a system that constructs verified neural networks for computer systems. Verified neural networks are neural networks that satisfy user-defined safety properties, called specifications. Ouroboros builds verified networks by a training-verification loop that combines deep learning training and neural network verification. Ouroboros introduces multiple techniques to fill the gap between today’s verification and the properties that systems require. Ouroboros also accelerates the training-verification loop by spec-aware learning. Our experiments show that ouroboros can train verified networks for all five applications that we study and has a 4.3× speedup on average compared with the vanilla training-verification loop.

### Used for
- safety

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety

### Techniques
- neural network verification techniques

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for Paper Scalable Verification of GNN-Based Job Schedulers

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7080246
- **Status:** Unknown
- **Last updated:** 2022-09-15T02:26:28.531445+00:00

### Description
Please follow the instructions in the readme to replicate the results in the paper.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Benchmark Sets for Variable Elimination in Conjunctions of Linear Real Arithmetic Constraints

- **Website:** N/A
- **DOI:** 10.5281/zenodo.10605373
- **Status:** Unknown
- **Last updated:** 2024-02-01T13:09:05.290314+00:00

### Description
Three benchmark sets for testing tools on the task of existential quantifier elimination from conjunctions of linear real arithmetic constraints (a.k.a. polyhedron projection).
All sets are given in three formats:

ine: .ine files as used by the CDD library and some other polyhedra libraries.
redlog: .red files as used by the CAS Reduce and its package Redlog
smtlib: .smt2 files as used by SMT related tools like SMT-RAT or z3.

The Random set contains random satisfiable conjunctions of 3-60 constraints with 3-30 variables and different coefficient densities, from which half of the variables are to be eliminated. The NN-Verif set contains conjunctions obtained in neural network verification tasks. The SMT-lib-deriv set contains conjunctions derived during SMT-solving of the QF_LRA satisfiability checking benchmarks from SMT-lib.

### Used for
(none)

### Input formats
- SMT-LIB
- SMT

### Supported languages
(none)

### Supported inputs
- SMT-LIB
- SMT

### Properties verified
(none)

### Techniques
- neural network verification techniques
- SMT solving

### External tools
- Z3

### Examples
(none)

### References
(none)


---

## ravenbeutner/astnar: First Release of Astnar

- **Website:** N/A
- **DOI:** 10.5281/zenodo.4682811
- **Status:** Unknown
- **Last updated:** 2021-04-13T12:27:24.255564+00:00

### Description
Tools for computing lower bounds on the probability of termination and the almost-sure termination (AST) verification of non-affine recursive programs.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Modular Termination Verification: Machine-Checked Proofs

- **Website:** N/A
- **DOI:** 10.5281/zenodo.1248801
- **Status:** Unknown
- **Last updated:** 2024-08-02T16:01:50.746610+00:00

### Description
Machine-checked using Coq 8.6.

Contents:


	Generic Utility Concepts

	
		Util: Notations for lists and decidable equality
	
	
	Module Correctness
	
		Programs: The syntax of programs. Parameterized over the set of types, values, and operators, and the well-founded type of levels.
		ProgramExecution: Relates programs to outcomes (termination with a result value or divergence).
		ProgramCorrectness: Correctness of a class, and correctness of a program in terms of correctness of its classes.
		WellTyped: Well-typedness of a program. Implies that the import graph is acyclic.
		Soundness: Correct well-typed programs do not diverge.
	
	
	Specification Style
	
		NonWf: Relates well-foundedness to descending chains. Used by WellOrderingTheoremEx.
		WellOrderingTheoremEx: Each well-founded relation can be extended to a well-ordering.
		MultisetOrder: Finite multisets, the Dershowitz-Manna ordering, and a proof of its well-foundedness.
		SpecStyle: Instantiates the syntax of programs with a well-founded (in fact: well-ordered) type of method bags.
		MethodBagLemmas: Some lemmas about method bag order, useful for the example correctness proofs.
	
	
	Example Programs
	
		Loopy: An example program that performs infinite inter-module recursion through dynamic binding.
		PlusOneFunc: An example program with dynamic binding that terminates.
		ExamplesWellTyped: Loopy and PlusOneFunc are well-typed.
		ProgramExecutionTests: Loopy diverges; PlusOneFunc has an execution that terminates with result 0.
		PlusOneFunc_is_Correct: A modular proof of correctness of PlusOneFunc.
		PlusOneFunc_terminates: Applies the soundness theorem to obtain that PlusOneFunc does not have diverging executions.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Formal Methods for NFA Equivalence: QBFs, Witness Extraction, and Encoding Verification

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6896218
- **Status:** Unknown
- **Last updated:** 2022-07-25T01:49:11.171442+00:00

### Description
Supplemental material to the paper.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Making IP = PSPACE Practical: Efficient Interactive Protocols for BDD Algorithms – Artifact

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7877702
- **Status:** Unknown
- **Last updated:** 2023-04-29T02:26:43.611281+00:00

### Description
This is the artifact for the submission “Making IP = PSPACE Practical: Efficient Interactive Protocols for BDD Algorithms”. Within the paper, we develop a new approach to interactively certify BDD algorithms. We implemented this approach as `blic`, a certifying QBF solver. This tool is evaluated against other QBF solvers.

The artifact consists of the source code for `blic`, as well as the data and other tools necessary to replicate the empirical claims of the paper.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
- SMT solving

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Supplementary code availability

- **Website:** N/A
- **DOI:** 10.5281/zenodo.15758068
- **Status:** Unknown
- **Last updated:** 2025-07-08T16:31:30.174961+00:00

### Description
# QBF: Quantum Biological Field Framework for Mechanistic Prediction of IDP Diseases
This project implements **QBF (Quantum Biological Field)** framework to uncover **disease-driving mechanisms** and **pathogenic sites** in **intrinsically disordered proteins (IDPs)**.
## Features
- **Mechanism-Oriented**    Predicts disease-specific conformational transitions and pathogenic residue hotspots.
- **Theoretical Integration**    Embeds residue-pair interactions for iterative refinement of hidden-state distributions.
- **No Retraining Required**    Generalizes across IDP families and disease variants without retraining, using only sequence input.
- **Experimentally Validated**    Predictions are supported by site-directed mutagenesis, aggregation assays, and Alzheimer’s disease models.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## General Boolean Formula Minimization with QBF Solvers

- **Website:** N/A
- **DOI:** 10.3233/FAIA230705
- **Status:** Unknown
- **Last updated:** 2024-07-06T22:00:18.423440+00:00

### Description
The minimization of propositional formulae is a classical problem in logic, whose first algorithms date back at least to the 1950s with the works of Quine and Karnaugh. Most previous work in the area has focused on obtaining minimal, or quasi-minimal, formulae in conjunctive normal form (CNF) or disjunctive normal form (DNF), with applications in hardware design. In this paper, we are interested in the problem of obtaining an equivalent formula in any format, also allowing connectives that are not present in the original formula. We are primarily motivated in applying minimization algorithms to generate natural language translations of the original formula, where using shorter equivalents as input may result in better translations. Recently, Buchfuhrer and Umans have proved that the (decisional version of the) problem is Σcomplete. We analyze three possible (practical) approaches to solving the problem. First, using brute force, generating all possible formulae in increasing size and checking if they are equivalent to the original formula by testing all possible variable assignments. Second, generating the Tseitin coding of all the formulae and checking equivalence with the original using a SAT solver. Third, encoding the problem as a Quantified Boolean Formula (QBF), and using a QBF solver. Our results show that the QBF approach largely outperforms the other two.

### Used for
(none)

### Input formats
- CNF
- QBF

### Supported languages
(none)

### Supported inputs
- CNF
- QBF

### Properties verified
(none)

### Techniques
- SMT solving

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for Paper Search-Space Pruning with Int-Splits for Faster QBF Solving

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7753526
- **Status:** Unknown
- **Last updated:** 2023-03-21T14:26:40.808393+00:00

### Description
This is the artifact for the paper "Search-Space Pruning with Int-Splits for Faster QBF Solving" submitted to the SAT2023 conference.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Software Artifact Accompanying the Article "Modular Verification for Almost-Sure Termination of Probabilistic Programs"

- **Website:** N/A
- **DOI:** 10.5281/zenodo.3363977
- **Status:** Unknown
- **Last updated:** 2020-01-25T07:23:58.298070+00:00

### Description
This package contains code and data needed for reproducing results reported in the following paper:

 

Modular Verification for Almost-Sure Termination of Probabilistic Programs
M. Huang, H. Fu, K. Chatterjee, A. Goharshady

To appear in OOPSLA 2019

### Used for
- termination

### Input formats
(none)

### Supported languages
- Java

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## peitl/qfun-sms: SMS

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14528836
- **Status:** Unknown
- **Last updated:** 2024-12-19T15:21:22.491660+00:00

### Description
Support for SAT Modulo Symmetries for isomorph-free graph generation subject to QBF constraints. See also the AAAI 2025 paper titled "Breaking Symmetries in Quantified Graph Search: A Comparative Study."

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## fslivovsky/qute: v1.2.0

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14536421
- **Status:** Unknown
- **Last updated:** 2024-12-20T14:25:30.235177+00:00

### Description
Support for SAT Modulo Symmetries for isomorph-free graph generation subject to QBF constraints. See also the AAAI 2025 paper titled Breaking Symmetries in Quantified Graph Search: A Comparative Study.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## ReBAC Availability Verifiers

- **Website:** N/A
- **DOI:** 10.5281/zenodo.56133
- **Status:** Unknown
- **Last updated:** 2025-04-24T07:28:45.676864+00:00

### Description
This is the implementation of Availability Criteria (Satisfiability, Feasibility and Resiliency) Verifiers for Relationship-based Access Control with support for Multiple Ownership (ReBAC/MO). The following are informal examples of availability criteria.

. Satisfiability: "Object o shall be accessible by at least 35 users in the current protection state."

. Resiliency: "Even if I were to recruit 10 additional patients (or lose 10 of my existing patients), object o shall remain accessible by at least 25 users."

. Feasibility: "I shall be able to make object o accessible by at least 50 users if the company hires no more than 10 additional colleagues (or fires no more than 10 existing colleagues)."

The ReBAC/MO consists of the Boolean combinations of atomic policies. The atomic policies are represented by a 2-tuple; comprising a Birooted graph pattern (one root represents the owner, the other one represents the requester) and a vertex in the social graph, to which the owner in the graph pattern will be anchored. The availability criteria then boils down to finding the graph pattern(s) in the social graph that are isomorphic to the graph patterns in the atomic policies. The verifiers use different technologies as to decide availability criteria. Below we briefly explain each verifier.

. In the first verifier we reduce the Availability Criteria (esp. Satisfiability) to Quantified Boolean Formula Satisfiability (QBF) and compile it into a non-prenex non-CNF format (QCIR). Please note, each atomic policy can be seen as an stand-alone Subgraph Isomorphism problem, hence, we use a fairly standard approach to reduce it to a Boolean Satifiability problem. The Boolean combination of Boolean Satisfiability problem (esp. with negations) yields a non-CNF QBF. A non-clausal QBF solver like RAReQS-NN or GhostQ can then be invoked to decide the availability criteria. 

. In the second verifier we employ an approach similar to the previous one. In nutshell, we reduce atomic policies to SAT problems and call a SAT solver (i.e. Sat4J) to solve it. Then we construct the original policy from the atomic policies and check if it is satisifiable.

. In the third verifier we adopt a completely differnet approach. We reduce the availability criteria into an Answer Set Programming problem. Then an ASP solver (i.e. clingo) is invoked to decide the availability criteria.

Please refer to the following paper for further readings:

Pooya Mehregan and Philip W. L. Fong. Policy Negotiation for Co-owned Resources in Relationship-Based Access Control. In the Proceedings of 21st ACM Symposium on Access Control Models and Technologies (SACMAT 2016), Shanghai, China, June 6-8, 2016.

Enjoy!

Pooya

### Used for
(none)

### Input formats
- CNF
- QBF

### Supported languages
(none)

### Supported inputs
- CNF
- QBF

### Properties verified
(none)

### Techniques
- neural network verification techniques
- SMT solving

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for Paper ParaQooba: A Fast and Flexible Framework for Parallel and Distributed QBF Solving

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7554207
- **Status:** Unknown
- **Last updated:** 2023-01-20T14:26:34.328426+00:00

### Description
The artifact for the paper "ParaQooba: A Fast and Flexible Framework for Parallel and Distributed QBF Solving" submitted to the TACAS2023 artifact evaluation.

We thank the reviewers for their comments and added the missing dependencies to this revised version. No other parts have been changed.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## 2LS

- **Website:** N/A
- **DOI:** 10.5281/zenodo.10184626
- **Status:** Unknown
- **Last updated:** 2023-11-22T09:35:45.866660+00:00

### Description
2LS ("tools") is a verification tool for C programs. It is built upon the CPROVER framework (cprover.org), which supports C89, C99, most of C11 and most compiler extensions provided by gcc and Visual Studio. It allows verifying array bounds (buffer overflows), pointer safety, exceptions, user-specified assertions, and termination properties. The analysis is performed by template-based predicate synthesis and abstraction refinements techniques.The uploaded archive is a submission used for SV-COMP 2024.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Code, Benchmarks, Data from the ICAPS 2022  paper "Classical Planning as QBF without Grounding"

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6367524
- **Status:** Unknown
- **Last updated:** 2022-03-20T01:49:39.701574+00:00

### Description
This submission contains three parts:


	Software/code: A copy of Q-Planner, a QBF based planner which avoids grounding, which is used for the experiments in the ICAPS-2022 paper.
	Benchmarks: All the benchmarks used in the experiments for the paper.
	Data: The data from 4 planners on all benchmarks along with statistics from Grendel cluster.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## A Practical Extension Mechanism for Decision Procedures: the Case Study of Universal Presburger Arithmetic

- **Website:** N/A
- **DOI:** 10.3217/jucs-007-02-0124
- **Status:** Unknown
- **Last updated:** 2024-07-16T06:15:59.564424+00:00

### Description
In this paper, we propose a generic mechanism for extending decision procedures by means of a lemma speculation mechanism. This problem is important in order to widen the scope of decision procedures incorporated in state-of-the-art verification systems. Soundness and termination of the extension schema are formally stated and proved. As a case study, we consider extensions of a decision procedure for the quantifier-free fragment of Presburger Arithmetic to significant fragments of non-linear arithmetic.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## 2LS

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7467706
- **Status:** Unknown
- **Last updated:** 2022-12-22T02:26:53.492730+00:00

### Description
2LS ("tools") is a verification tool for C programs. It is built upon the CPROVER framework (cprover.org), which supports C89, C99, most of C11 and most compiler extensions provided by gcc and Visual Studio. It allows verifying array bounds (buffer overflows), pointer safety, exceptions, user-specified assertions, and termination properties. The analysis is performed by template-based predicate synthesis and abstraction refinements techniques.

The uploaded archive is a submission used for SV-COMP 2023.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Automated Temporal Verification for Algebraic Effects

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7108627
- **Status:** Unknown
- **Last updated:** 2024-07-16T02:00:52.067799+00:00

### Description
Although effect handlers offer a versatile abstraction for user-defined effects, they produce complex and less restricted execution traces due to the composable non-local control flow mechanisms. This paper is interested in the temporal behaviors of effect sequences, such as unhandled effects, termination of the communication, safety, fairness, etc. Specifically, we propose a novel effects logic ContEffs, to write precise and modular specifications for programs in the presence of user-defined effect handlers and primitive effects. As a second contribution, we devise a forward verifier together with a fixpoint calculator to infer the behaviors of such programs. Lastly, our automated verification framework provides a purely algebraic term-rewriting system (TRS) as the back-end solver, efficiently checking the entailments between ContEffs assertions. To demonstrate the feasibility of our proposals, we prototype a verification system where zero-shot, one-shot, and multi-shot continuations coexist; prove its correctness; present experimental results; and report on case studies.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
- OCaml
- C

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
- SMT solving

### External tools
- Z3

### Examples
(none)

### References
(none)


---

## Legal Grounds for Establishment and Termination of Business Associations

- **Website:** N/A
- **DOI:** 10.5281/zenodo.3229082
- **Status:** Unknown
- **Last updated:** 2024-07-22T22:54:53.648209+00:00

### Description
It is known that establishment of associations of business entities is included to the mechanisms for ensuring of favorable conditions for development of modern market relations. Their role increases every year but there are no clear provisions in legislation about the notion of associations of legal entities as well as there is no single direction for development of legal regulation of relations regarding their activities.

According to the Commercial Code of Ukraine legal entities have the right to unite their own activities based on the agreement (particularly joint operation agreement) and by establishing new entities (particularly joint companies).

Joint companies play an important role among members of commercial relations.

Procedures of consolidating funds and concentrating production which take place in modern Ukrainian economy contribute to business associations. In spite of their active participation in commercial relations and taking into account historical and economic conditions of their activities legal regulation of organization and activities of business associations in various business spheres are inadequate because:

i) there are incompliances in legislation regarding business associations; 

ii) on practice one can see that associations are established and exist in the forms which are not provided for by Ukrainian legislation such as business group, the group of companies, financial and industrial group etc. They are not legally formalized, registered, do not have clear rights and duties of members, legal status of property etc.

Certain issues which shall be regulated in legislation relate to establishment and activities of business associations such as procedure of managing the state association; differentiation of authorities between the Cabinet of Ministers of Ukraine and central executive agencies regarding establishment of the state associations, approval of the articles of association, appointment of managers etc.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Reducing Acceptance Marks in Emerson-Lei Automata by QBF Solving

- **Website:** N/A
- **DOI:** 10.4230/LIPIcs.SAT.2023.23
- **Status:** Unknown
- **Last updated:** 2024-07-15T09:20:32.955276+00:00

### Description
This paper presents a novel application of QBF solving to automata reduction. We focus on Transition-based Emerson-Lei automata (TELA), which is a popular formalism that generalizes many traditional kinds of automata over infinite words including Büchi, co-Büchi, Rabin, Streett, and parity automata. Transitions in a TELA are labelled with acceptance marks and its accepting formula is a positive Boolean combination of atoms saying that a particular mark has to be visited infinitely or finitely often. Algorithms processing these automata are often very sensitive to the number of acceptance marks. We introduce a new technique for reducing the number of acceptance marks in TELA based on satisfiability of quantified Boolean formulas (QBF). We evaluated our reduction technique on TELA produced by state-of-the-art tools of the libraries Owl and Spot and by the tool ltl3tela. The technique reduced some acceptance marks in automata produced by all the tools. On automata with more than one acceptance mark obtained by translation of LTL formulas from literature with tools Delag and Rabinizer 4, our technique reduced 27.7% and 39.3% of acceptance marks, respectively. The reduction was even higher on automata from random formulas.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Replication Package for the paper: Verification of Distributed Systems via Sequential Emulation

- **Website:** N/A
- **DOI:** 10.5281/zenodo.5348289
- **Status:** Unknown
- **Last updated:** 2021-09-15T13:48:24.971380+00:00

### Description
This package allows to replicate the experiments described in “Verification of Distributed Systems via Sequential Emulation”.

Instructions for full replication are also included.

Repository contents


	
	main.sh: Quickstart script to run all experiments
	
	
	permissions.sh: script to give adequate permissions to executables
	
	
	replication.tar.gz: gzipped archive containing:

	
		
		emergence, invariant, stock: C programs used in the experimental evaluation. Each directory also contains a _logs folder with the log files referred in the paper.
		
		
		labs: LAbS specifications used for emergence and invariant experiments.
		
		
		LICENSE: conditions to use the repository contents
		
		
		tools: Software used to generate C programs and run experiments
		
		
		README.mdown: the README file of the original replication repository (https://gitlab.inria.fr/ldistefa/tosem-artifacts)
		
		
		README-ZENODO.mdown: this document
		
		
		replication.py: Python script to replicate the experiments
		
		
		replication.sh: fallback shell script to replicate the experiments
		
	
	


Requirements

All experiments should run successfully on most x64 Linux machines. Python 3.7 or above is needed to run the replication.py script. Alternatively, one may run the replication.sh shell script.

Some caveats about specific tools:


	
	Symbiotic requires a python executable in the machine’s PATH (usually /usr/bin/python). This may be a symbolic link pointing to a Python 3 executable (usually /usr/bin/python3).
	
	
	SeaHorn requires a Python 2 executable (usually /usr/bin/python2).
	
	
	To generate instrumented programs (see below), an external C preprocessor is required. For instance, we use gcc -E. We do provide ready-to-use instumented programs.
	


Quickstart

Download the whole repository to some directory dir, then:

cd /path/to/dir
# Gives execution permission to main.sh, tools, and their dependencies
chmod +x permissions.sh 
# Unpacks the archive, makes log directories, and runs all experiments
./main.sh

The script will create a dir/logs directory with subdirectories emergence, invariant, and stock, where it will store the output of each verification task.

Replication details

Generation of C programs from LAbS specifications

The following commands will use sliver to create C emulation programs from each LAbS system considered in the paper:

# Invariant programs
tools/sliver-v1.5_linux_x64/sliver.py labs/formation.invariant.labs size=10 range=2 n=3 --fair --no-bv --show > invariant/formation/formation.c
tools/sliver-v1.5_linux_x64/sliver.py labs/approx.labs yes=1 no=2 --no-bv --show > invariant/approx-a/approx-a.c
tools/sliver-v1.5_linux_x64/sliver.py labs/approx.labs yes=2 no=3 --no-bv --show > invariant/approx-a/approx-b.c.orig
tools/sliver-v1.5_linux_x64/sliver.py labs/maj.labs yes=1 no=2 --no-bv --show > invariant/maj/maj.c.orig
# Emergence programs
tools/sliver-v1.5_linux_x64/sliver.py labs/boids.labs birds=3 size=5 delta=5 --fair --no-bv --show > emergence/boids/boids.c
tools/sliver-v1.5_linux_x64/sliver.py labs/flock.labs birds=3 size=5 delta=5 --fair --no-bv --show > emergence/flock/flock.c
tools/sliver-v1.5_linux_x64/sliver.py labs/formation.emergence.labs size=10 range=2 n=3 --fair --no-bv --show > emergence/formation/formation.c

Each folder under invariant and emergence contains a <program>.c file which is the output of one the above commands. Notice that, for approx-b and maj, we have manually performed some additional transformations. The unmodified sliver output is named maj.c.orig and the final program is named maj.c.

Instrumentation of C programs

SLiVER was originally tailored towards BMC verification, so it generates programs that can be directly verified by CBMC. Other tools require an instrumentation steps. Typically this amounts to replace verification intrinsics with those supported by the tools, add specific headers or function declarations, etc. We have automated this steps by means of a helper Python program called absentee, which can be found in the tools directory and at (https://github.com/lou1306/absentee)

Typically, to instrument the SLiVER program program.c for verification by a specific tool, one can use the following command line:

cd tools/absentee
gcc -E /path/to/<program>.c | python3 -m absentee --conf <tool>.conf - > /path/to/<program>.<tool>.c

Preprocessing the original program with gcc (or another compiler) is needed because absentee does not support preprocessor directives.

Each folder under invariant and emergence already contains a file <program>.<tool>.c, which is the result of this step for each tool in our experimental evaluation.

Verification

Each tool needs a specific set of arguments, environment variables, etc. to correctly perform its verification task. To investigate the actual commands we used in our evaluation, please check the replication.sh script or the replication.py program.

About the stock case studies

We wrote the stock-safe and stock-unsafe case studies directly as triple structure, and then encoded it as C programs using the same procedure described in the paper and implemented by sliver.

We provide these C programs, as well as their instumented version for 2ls, in the stock folder.

Usage instructions for replication.py

In case one wants more granularity, replication.py may be run manually. ./replication.py --help shows usage instructions. In brief:


	
	./replication.py runs all the experiments.
	
	
	./replication.py tool1 tool2 ... only runs the experiments with the given tools.
	
	
	./replication.py --list lists the tool names.
	
	
	./replication --timeout <n> overrides the default timeout to n seconds (n must be a positive integer)
	


By adding --dry-run, the script only shows the experiments’ command lines, without actually executing them. Keep in mind that most tools also require custom environment variables or won’t run properly when invoked outside of their own directories, so these command lines are only for reference.

Support

For further information, you may look at the original Git repository for the artifacts: (https://gitlab.inria.fr/ldistefa/tosem-artifacts)

You can also contact the paper’s corresponding author: Luca Di Stefano luca.di-stefano@inria.fr

Acknowledgments

Work partially funded by MIUR project PRIN 2017FTXR7S IT MATTERS (Methods and Tools for Trustworthy Smart Systems).

Disclaimer

The authors of this repository do not endorse using its contents for ANY purpose besides replication of experiments presented in the paper “Verification of Distributed Systems via Sequential Emulation”. Please enquire with the paper’s corresponding author (Luca Di Stefano luca.di-stefano@inria.fr) about software packages intended for generic usage.

### Used for
(none)

### Input formats
(none)

### Supported languages
- Python
- C

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
- CBMC

### Examples
(none)

### References
(none)


---

## QSOLE: Automated QBF Equivalence Checking

- **Website:** N/A
- **DOI:** 10.5281/zenodo.17356608
- **Status:** Unknown
- **Last updated:** 2025-10-29T13:12:02.494251+00:00

### Description
QSOLE: Automatic QBF Equivalence Checking
Introduction
This artifact was submitted by Peter Pfeiffer, Mark Peyrer, Daniel Große and Martina Seidl for the TACAS 2026 with the submission number 9062 aiming for Available, Functional and Reusable badges. It contains everything necessary to reproduce the examples shown in the corresponding paper alongside testcases to demonstrate basic functionality. In the following sections you will learn everything you need to know about this artifact and how to reproduce the experiments.
The input formulas used by tests are divided into four categories:

atleast contains at-least-k cardinality constraints with randomly generated quantifier prefixes and different encodings (km-totalizer and sequential counters).
eq contains equals-k cardinality constraints with randomly generated quantifier prefixes and different encodings (km-totalizer and sequential counters).
hein features Hein puzzles expressed with different encoding techniques from SQval.
paper contains the examples presented in the corresponding paper.

The artifact was published under the following DOI: 10.5281/zenodo.17356608
Structure and Content
The artifact has the following structure:/|--  expected|--  output|--  qsole|--  scripts|--  tests

expected contains the log-files of the experiments conducted with this artifact on our machine
output is the target of the results from the experiments and is connected to a local folder with the same name on the host-machine. The logfiles from the runs can be found there
qsole contains the c++ source code and build-environment for the QSOLE tool
scripts is a collection of bash-scripts in order to run the experiments. The one relevant for you are listed in the next section
tests contains the input formulas as well as the pcount for each check

Running the artifact
1. Setup Docker
A working docker environment installed on your machine is required. The docker container can be setup the following way:# download qsole-artifact.zst from zenododocker load < qsole-artifact.zstdocker run -v `pwd`/output:/output -itd --network none --name qsole_running1 qsole-artifactdocker exec -it qsole_running1 bash
The first line loads the docker-image from the the export, the second will create a container using the image and the last connects your current terminal to the container.
In order to leave the container, just execute exit.
Furthermore, you can call docker stop qsole_running1docker rm qsole_running1
to stop and delete the running container.
Important: Please ensure to have a working docker setup, with your user added to the docker group. This can be verified using docker ps. If there are no errors, your environment should be in working order.
 
2. Run the Smoke Test
We prepared a small script for you to check, if the tool was installed successfully. This is just for your convenience, please feel free to use any of the provided ressources to conduct the smoke test.
The script /scripts/smoke_test.sh will execute the following code
/qsole/build/qsole --help/qsole/build/qsole /test/paper_example/phi.qdimacs /test/paper_example/psi.qdimacs 3 --check sole --subsumption --info --noskipi.e. printing the help-text and then solve the minimal example presented in the paper using a full Solution Equivalence Check.The following output is to be expected, if the artifact is up and running.
qsole v0.1 - a checker qbf solution equivalenceusage: qsole FORMULA1 FORMULA2 PCOUNT [OPTIONS...]
FORMULA1 expects a file containing a QDIMACS encoded QBFFORMULA2 expects a file containing a QDIMACS encoded QBFPCOUNT expects the length of the common prefixThe following values for OPTIONS are valid:  -h, --help           displays this command  --check <VALUE>      specifies the check to be made (skent|sole|psole|skeq) [default: skent]  --ouput <PATH>       outputs the encoding to the specified path  --models             if specified, models will be printed if suitable    --subsumption        if specified, eliminate subsumptions before encoding  --noskip             if specified, all checks will be done even if the result is already clear  --quiet              does not print any logging messages, not even errors  --info               increases verbosity level to "info"[QSOLE] [INF] Skolem Entailment f1 |=SK f2 resulted in 10[QSOLE] [INF] Skolem Entailment f2 |=SK f1 resulted in 20[QSOLE] [INF] Skolem Entailment !f1 |=SK !f2 resulted in 10[QSOLE] [INF] Skolem Entailment !f2 |=SK !f1 resulted in 10[QSOLE] [INF] Solution Equivalence (f1 <->SOL f2) resulted in 20
3. Run the Experiment
While connected, you can run one of the following scripts to generate log-files.The output can be found in the output folder.
The following requirements were measured on a host machine for the docker container with the following specifications:

Intel Core i7-1355U Prozessor
32 GB RAM
Intel Iris Xe GPU




Script
Description
est. time


/scripts/atleast_psole.sh
Solution Equivalence of atleast
~150ms


/scripts/atleast_full.sh
All checks of atleast
~350ms


/scripts/eq_psole.sh
Solution Equivalence of eq
~750ms  


/scripts/eq_full.sh
All checks of eq
~1.5s


/scripts/hein_psole.sh
Solution Equivalence of hein
~45s


/scripts/hein_full.sh
All checks of hein
~150s


/scripts/paper_psole.sh
Solution Equivalence of paper ex.
<10ms


/scripts/paper_full.sh
All checks of paper ex.
~20ms


/scripts/all.sh
All checks of this artifact
~200s



 
Dependencies
The following core-dependencies are required to run this artifact.Note that this is soley for information purpose, those do not have to be installed manually.For a more detailed list we want to refer to the Dockerfile in the sources, where the whole artifact can be reproduced from scratch.Each of the used tool has a licence within its source files.
Third Party Tools used by QSOLE:

DepQBF v6.03
CaDiCaL v2.1.3
Nenofex v1.1 (Included in DepQBF)
Picosat v965 (Included in DepQBF)

 
Needed for Building:

Docker image ubuntu:24.04
GCC for C++ (g++) compiler
CMake

### Used for
(none)

### Input formats
- QBF

### Supported languages
- C

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## 2LS: Arrays and Loop Unwinding

- **Website:** N/A
- **DOI:** 10.1007/978-3-031-30820-8_31
- **Status:** Unknown
- **Last updated:** 2024-07-15T09:20:36.022915+00:00

### Description
2LS is a C program analyser built upon the CPROVER infrastructure that can verify and refute program assertions, memory safety, and termination. Until now, one of the main drawbacks of 2LS was its inability to verify most programs with arrays. This paper introduces a new abstract domain in 2LS for reasoning about the contents of arrays. In addition, we introduce an improved approach to loop unwinding, a crucial component of the 2LS’ verification algorithm, which particularly enables finding proofs and counterexamples for programs working with dynamic memory.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Symbiotic 7: Integration of Predator and More (Competition Contribution)

- **Website:** N/A
- **DOI:** 10.5281/zenodo.3678328
- **Status:** Unknown
- **Last updated:** 2020-02-21T19:20:56.183012+00:00

### Description
Symbiotic is a tool for finding bugs in programs that combines fast static analyses with instrumentation, program slicing, and symbolic execution. This artifact contains Symbiotic 7 in the version that competed in Software Verification Competition (SV-COMP) 2020.

Symbiotic 7 brings improvements in all parts of the tool. In particular, we integrated the advanced shape analysis implemented in Predator to our instrumentation process for memory safety checking. Further, we extended our slicer to correctly handle non-terminating programs. This new slicing is applied in termination analysis, where we also added instrumentation for the detection of simple cycles in the program state space. The witness generation process changed as well.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The Octave-State Formalism: A State-Space Representation of Computational Loops

- **Website:** N/A
- **DOI:** 10.5281/zenodo.17045972
- **Status:** Unknown
- **Last updated:** 2025-09-03T11:18:38.410384+00:00

### Description
This paper introduces the Octave-State Formalism, a novel theoretical framework for the analysis of computational loops. Moving beyond the classical, one-dimensional view of iteration, this formalism models a loop's execution as the discrete-time evolution of a state vector within an eight-dimensional abstract space. Each dimension of this "Octave-State" corresponds to a fundamental aspect of the loop's behavior, including its temporal progression, data transformation, causal dependencies, resource consumption, concurrency potential, numerical stability, control flow path, and termination horizon. By leveraging the mathematical rigor of state-space representation from control theory and drawing conceptual parallels with principles from theoretical physics—such as dimensional regularization, phase space, and the many-worlds interpretation—this paper develops a unified model. We demonstrate that this formalism provides a more holistic understanding of loop dynamics, offering new geometric insights into complex problems like data dependency analysis, loop-level parallelism, and formal verification through loop invariants. The Octave-State Formalism is presented not merely as a descriptive tool, but as a generative framework for the design and automated analysis of next-generation algorithms and high-assurance software systems.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Toward Determining NFA Equivalence via QBFs

- **Website:** N/A
- **DOI:** 10.5281/zenodo.4279875
- **Status:** Unknown
- **Last updated:** 2020-11-19T00:27:05.875267+00:00

### Description
Equivalence of deterministic finite automata (DFAs) has been researched for several decades, but equivalence of nondeterministic finite automata (NFAs) is not as studied.  Equivalence of two NFAs is a PSPACE-complete problem.  NFA quivalence is a challenging theoretical problem with practical applications such as lexical analysis.  Quantified boolean formulas (QBFs) naturally encode PSPACE-complete problems, and we share our preliminary work towards determining NFA equivalence via QBFs.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## FSE2022benchmarks/termination: FSE2022benchmark-termination

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6548039
- **Status:** Unknown
- **Last updated:** 2022-05-14T13:50:23.382140+00:00

### Description
Benchmarks and result-files for paper "Large-Scale Analysis of Non-Termination Bugs in Real-World OSS Projects" (FSE-2022)

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for (Semantic) Feature Model Differences with (Q)SAT

- **Website:** N/A
- **DOI:** 10.5281/zenodo.15338222
- **Status:** Unknown
- **Last updated:** 2025-05-04T20:35:41.422740+00:00

### Description
Author Information

Names: Simone Heisinger, Maximilian Heisinger, Martina Seidl
Affiliations: Johannes Kepler University Linz, Institute for Symbolic AI
Emails: simone.heisinger@jku.at, maximilian.heisinger@jku.at, martina.seidl@jku.at

Associated Paper Information

Title: (Semantic) Feature Model Differences with (Q)SAT
Abstract: Feature models evolve in multiple iterations over time. When modellers change a model, they enact syntactical changes in order to produce specific semantic differences between model iterations. Many tools have been developed to analyze such syntactical differences, but the changing semantics of models were harder to assess. Tools for semantic differences between feature model iterations rely on Binary Decision Diagrams (BDDs) or encode each change into SAT, the former leading to BDD scaling issues and the latter requiring editor support or other specialized tooling. We contribute the first concise formalization of feature models and their semantic differences into propositional logic and use it to efficiently and scalably classify semantic differences using SAT solvers. We then extend our definition into QSAT in order to quantify the full list of semantic differences between feature models and enumerate them using QBF tools, without needing specialized feature model solvers. We implement a semantic difference classifier using our UVL processing pipeline based on Booleguru (instead of the more widely used FeatureIDE) and evaluate it on industrial feature model instances in the standardized UVL format. We also evaluate our QSAT-based semantic difference enumerator and reproduce prior results. We provide all software and evaluation results in an artifact.

Documentation
The code comes from these upstream repositories:

https://gitlab.sai.jku.at/booleguru/booleguru
https://gitlab.sai.jku.at/maximaximal/outer-count
https://github.com/arminbiere/kissat
https://github.com/lonsing/depqbf

The artifact contains:

the necessary software to run the experiments (booleguru, outercount, kissat, compare.sh)
a script quick-test.sh to see if all software is correctly installed
test-formula-uvl.uvl and test-formula-dimacs.dimacs which are needed for quick-test.sh
the scripts reproduce-table1.sh, reproduce-table2.sh, reproduce-table3.sh and reproduce-table4.sh to generate the output from the corresponding tables in the paper (Semantic) Feature Model Differences with (Q)SAT
in bigfiles/ are all .uvl files used in the evaluation (original files can also be downloaded from uvlhub.io). The modified versions of each formula are names _mov.uvl which indicate that some part of the formula was moved
applet1.uvl and applet2.uvl represent the running example from the paper Feature Model Differences from 2012
bike1.uvl and bike2.uvl represent the running example from our paper
when using the sources without docker, we provide the compiled binaries for x64 Linux in bin-linux-amd64. This also includes a setup-path.sh script to set the $PATH variable. For more detailed information on this see our DETAILS.html.
the results (classifications and runtimes) for table 3 in the paper from the original run. For more detailed information on this see the DETAILS.html
a DETAILS.org/DETAILS.html with more detailed information on the commands used in the scripts: DETAILS.html, its markup version is in DETAILS.org.
a Dockerfile to run the software and tests in, using Docker, Podman, or some other software.



Artifact Evaluation Environment
System Specifications Used by Authors

Operating System: Ubuntu 24.04
CPU: AMD EPYC 7313
Memory: 256 GB
Disk Space: 10 GB
GPU (if applicable): none

Estimated Hardware Requirements for Evaluation

Minimum required CPU: any
Minimum required Memory: 8 GB
Minimum required Disk Space: 10 GB
Minimum required GPU (if applicable): none

Software Requirements

Podman or Docker (the former often is readily available in package repositories)

Compatibility Considerations

Known compatibility issues of the container/VM: Untested on Windows

Kick-the-Tires
To run the container with the provided zst using Podman:

podman load < fmdiff-container.tar.zst
podman run -ti --replace --name fmdiff localhost/fmdiff

To fully rebuild the container, use the following:

podman build . -t fmdiff
podman run -ti --replace --name fmdiff localhost/fmdiff

If opening the provided container, change your directory into artifact using cd artifact before running the mentioned scripts.
To check all tools if they are working correctly after the setup, run the provided script ./quick-test.sh.
There, all tools should display some output. The correct output is provided directly after the tool's output. Please confirm if the tool output and the expected output match. The output could be out of order, this has no impact on the functionality of the artifact.
the checks included in quick-test.sh are:

booleguru working test
kissat working test
outercount working test
compare.sh working test

For the bigger evaluations, increase the stack size using ulimit -s 800000. This is done automatically in the reproduce-table3.sh script, but has to be done manually once for each terminal session if you decide to do further evaluations.
If booleguru is aborting with errors, most likely the stack size was too small, which happens if it stays at the default. The error comes from the kernel not allowing booleguru's stack to grow forever. Booleguru's design has some recursive functions that need a bigger stack size for some operations.
Full Evaluation
If opening the provided container, change your directory into artifact using cd artifact before running the mentioned scripts.
Table 1
To reproduce table 1 from the paper (configurations which are allowed in bike2 but not in bike1):
run the script reproduce-table1.sh with ./reproduce-table1.sh
This prints the 4 configurations mentioned in the paper in table 1. NOTE: the lines in the table featured in the paper are rearranged and for better human reading include some spacing. The output from this script contains the same information as in the table in the paper.
The estimated runtime is less than a few seconds.
Table 2
To reproduce table 2 from the paper (configurations which are allowed in bike1 but not in bike2):
run the script reproduce-table2.sh with ./reproduce-table2.sh
This prints the 5 configurations mentioned in the paper in table 2. NOTE: the lines in the table featured in the paper are rearranged and for better human reading include some spacing. The output from this script contains the sam information as in the table in the paper.
The estimated runtime is less than a few seconds.
Table 3
To reproduce table 3 from the paper (times to classify edits and if a classification applies):
run the script reproduce-table3.sh with ./reproduce-table3.sh
This prints for every feature model name mentioned in table 3 in the paper the classification and how long it took to get that classification. So each cell from the paper is printed with the script like this:

============================================
= automotive01
============================================

=== automotive01 generalization ===
booleguru "!(" "bigfiles/automotive01.uvl" "<-" "bigfiles/automotive01_mov.uvl" ")" --dimacs
bigfiles/automotive01.uvl <- bigfiles/automotive01_mov.uvl ===== 1
bigfiles/automotive01.uvl is not a generalization of bigfiles/automotive01_mov.uvl

real	0m1,507s
user	0m1,486s
sys	0m0,019s

From this we can see that for automotive01 it checks if it is a generalization or not. The last line of text says bigfiles/automotive01.uvl is not a generalization of bigfiles/automotive01_mov.uvl so it is not a generalization. The time which is important for the table is real 0m1,507s. Times can change depending on used hardware, the important part is that for the strict-generalization and strict-specialization the runtime should be around double that of the non strict version if the non strict check holds. This means that for automotive01 and financialservices01 since generalization and specialization do not hold, all five times should be around the same. For all other names in the table (automotive02_01, automotive02_02, automotive02_03, automotive02_04, ea2468, linux-2.6.33.3) strict-generalization and strict-specialization should take around double the time generalization and specialization take. Relative differences between the files should be similar compared to in the paper.
The estimated runtime depends on the hardware used, with a regular laptop with a recent Intel CPU and 16GB of RAM the whole script runs for about 5 minutes.
In the folder results are the times with the tested setup which are the times mentioned in the paper.
Table 4
To reproduce table 4 from the paper (configurations which are allowed in applet1 but not in applet2):
run the script reproduce-table4.sh with ./reproduce-table4.sh
This prints the 4 configurations mentioned in the paper in table 4.
The estimated runtime is less than a few seconds.

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## General Boolean Formula Minimization with QBF Solvers

- **Website:** N/A
- **DOI:** 10.3233/FAIA230705
- **Status:** Unknown
- **Last updated:** 2024-07-06T22:00:29.530867+00:00

### Description
(none)

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Security Type Checking for MILS-AADL Specifications

- **Website:** N/A
- **DOI:** 10.5281/zenodo.47989
- **Status:** Unknown
- **Last updated:** 2024-08-04T04:12:36.664620+00:00

### Description
Information flow policies are widely used for specifying confidentiality and integrity requirements of security-critical systems. In contrast to access control policies and security protocols, they impose global constraints on the information flow and thus provide end-to-end security guarantees. The information flow policy that is usually adopted is non-interference. It postulates that con dential data must not affect the publicly visible behavior of a system. However, this requirement is usually broken in the presence of cryptographic operations. 

In this paper, we provide an extended definition of non-interference for systems that are specified in a MILS variant of the Architecture Analysis and Design Language (AADL). More concretely, we propose a type system for MILS-AADL component definitions that distinguishes between breaking non-interference because of legitimate use of sufficientlynbsp;strong encryption and breaking non-interference due to annbsp;unintended information leak. To this aim, it tracks bothnbsp;intra- and inter-component information flow and considersbr /> both data- and event-flow security./p>

### Used for
- security

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- security

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## From Innermost to Full Almost-Sure Termination of Probabilistic Term Rewriting - AProVE Artifact

- **Website:** N/A
- **DOI:** 10.5281/zenodo.10787128
- **Status:** Unknown
- **Last updated:** 2024-07-06T23:32:11.505841+00:00

### Description
This is the artifact for AProVE's newest version for FoSSaCS24! In order to run the artifact, you can find an OVA file for a VM that has everything installed and is ready to go! Just open the VM with your favourite tool. On startup a terminal should open with further instructions. These instructions can also be found in the Readme.txt.
Additionally, you can find the necessary text files for the installation, requirements, and license of the artifact.
In this artifact, one can use the Automated Program Verification Environment (AProVE) in order to prove (innermost) almost-sure termination of probabilistic term rewrite systems (TRSs). TRSs are a very basic functional programming language which we use to analyze probabilistic algorithms mainly concerning (user-defined) data structures.
Inside the VM, AProVE is already installed, and you will find our benchmark set. Furthermore, the required SAT/SMT-Solvers for AProVE (MiniSat, Yices, Z3) are installed as well.

### Used for
- termination

### Input formats
- SMT

### Supported languages
- Java

### Supported inputs
- SMT

### Properties verified
- termination

### Techniques
- SMT solving

### External tools
- Z3

### Examples
(none)

### References
(none)


---

## Incremental Development of Real-Time Requirements: The Light Control Case Study

- **Website:** N/A
- **DOI:** 10.3217/jucs-006-07-0704
- **Status:** Unknown
- **Last updated:** 2024-07-16T06:16:13.638204+00:00

### Description
System requirements frequently change while the system is still under development. Usually this means going back and revising the requirements specification and redoing those development steps already completed. In this article we show how formal requirements can be allowed to evolve while system development is in progress, without the need for costly redevelopment. This is done via a formalism which allows requirements engineering steps to be interleaved with formal development steps in a manageable way. The approach is demonstrated by a significant case study, the Light Control System.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## RV-Match

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7464477
- **Status:** Unknown
- **Last updated:** 2023-01-20T10:40:20.845360+00:00

### Description
Docker image file containing the RV-Match tool installed in an Ubuntu Jammy container. Run:

docker load < rv-match-nfm-23.tar.gz

to install the image in your local environment.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Report of the Third QBF Solvers Evaluation1

- **Website:** N/A
- **DOI:** 10.3233/sat190019
- **Status:** Unknown
- **Last updated:** 2024-12-13T08:42:35.662272+00:00

### Description
n/a

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## TokenJoin: Efficient Filtering for Set Similarity Join with Maximum Weighted Bipartite Matching

- **Website:** N/A
- **DOI:** 10.14778/3574245.3574263
- **Status:** Unknown
- **Last updated:** 2024-07-12T16:07:42.417773+00:00

### Description
Set similarity join is an important problem with many applications in data discovery, cleaning and integration. To increase robustness, fuzzy set similarity join calculates the similarity of two sets based on maximum weighted bipartite matching instead of set overlap. This allows pairs of elements, represented as sets or strings, to also match approximately rather than exactly, e.g., based on Jaccard similarity or edit distance. However, this significantly increases the verification cost, making even more important the need for efficient and effective filtering techniques to reduce the number of candidate pairs. The current state-of-the-art algorithm relies on similarity computations between pairs of elements to filter candidates. In this paper, we propose token-based instead of element-based filtering, showing that it is significantly more lightweight, while offering similar or even better pruning effectiveness. Moreover, we address the top-𝑘 variant of the problem, alleviating the need for a user-specified similarity threshold. We also propose early termination to reduce the cost of verification. Our experimental results on six real-world datasets show that our approach always outperforms the state of the art, being an order of magnitude faster on average.

### Used for
- robustness
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- robustness
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Design and implementation of QASP Solver

- **Website:** N/A
- **DOI:** 10.5281/zenodo.5425783
- **Status:** Unknown
- **Last updated:** 2021-09-04T01:48:42.733274+00:00

### Description
We present, a new ASP solver called Quantifying over ASP, or briefly QASP, for ASP(Q) problems resolution, i.e. an extensive ASP formalism, inspired by Quantified Boolean Formula, which adds quantifiers over stable models, in order to model PSPACE problem.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
- SMT solving

### External tools
(none)

### Examples
(none)

### References
(none)


---

## FSE2022benchmarks/-FSE-2022-Termination: FSE2022-Termination

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6548310
- **Status:** Unknown
- **Last updated:** 2022-05-14T13:50:27.233099+00:00

### Description
Benchmarks and result-files for paper "Large-Scale Analysis of Non-Termination Bugs in Real-World OSS Projects" (FSE-2022)

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for article "Reflections on Termination of Linear Loops"

- **Website:** N/A
- **DOI:** 10.5281/zenodo.4742843
- **Status:** Unknown
- **Last updated:** 2021-05-08T01:48:10.012648+00:00

### Description
This is the artifact for the CAV 2021 paper, “Reflections on Termination of Linear Loops”. The artifact provided is an OVA virtual machine that can be opened via VirtualBox. The operating system is Ubuntu 18.04 LTS. It contains an installation of the tool as described in the paper, and the benchmark suites we have used to evaluate the tool. It also contains installations of benchexec and ComPACT, Ultimate Automizer, 2LS, CPAchecker for easy reproduction of results in the Evaluation section of the paper.

### Used for
- termination

### Input formats
- C source

### Supported languages
- C

### Supported inputs
- C source

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The Efficacy and Safety of Extraamniotic Mannitol along with Carboprost (PGF2α) and Intracervical Misoprostol (PGE1) in Second Trimester Termination of Pregnancy: A Prospective Comparative Clinical Study

- **Website:** N/A
- **DOI:** 10.5281/zenodo.12679117
- **Status:** Unknown
- **Last updated:** 2024-07-07T09:50:18.760535+00:00

### Description
Introduction: Second trimester termination of pregnancy accounts for around 10 to 15% of all abortions annually. These can be performed either medically or surgically. The aim of this study is to compare the efficacy and safety of extraamniotic mannitol along with carboprost (PGF2α) and intracervical misoprostol in second trimester termination of pregnancy. Result: The most common indication for termination of pregnancy was intrauterine fetal demise (41.7% in mannitol group and 45.8% in misoprostol group). Second trimester termination of pregnancy success rate was significantly higher in the extra-amniotic mannitol along with PGF2α group as compared to intracervical misoprostol group (95.8% v/s 75%, p<0.05).A significantly shorter duration from induction to delivery was observed in the extra-amniotic mannitol along with PGF2α group as compared to intracervical misoprostol group (19.3 ± 4.2 v/s 22.3 ± 2.1 hours, p<0.01).Incidence of side effects like pyrexia, diarrhea, abdominal pain and headache were significantly lower in the mannitol group as compared to misoprostol group. Conclusion: Extra-amniotic mannitol along with carboprost (PGF2α) is an effective and safe method for second trimester termination of pregnancy. The success rate of extra amniotic mannitol along with PGF2α was significantly higher with notably shorter induction-abortion interval. A remarkable lower hospital stay and fewer side effects were seen in patients induced by mannitol along with PGF2α.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## A special view on the method of implication, classification, and decision-making strategies of the human body channels

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7109863
- **Status:** Unknown
- **Last updated:** 2024-07-16T01:58:44.862671+00:00

### Description
The fast development of semiconductor technology and method scaling over a couple of many years has enabled the prolific increase of small-form issue wearable gadgets and physiological sensors. Those devices are connected to every different thru radio frequency conversation via air medium, and form a network of interconnected devices around the human body, normally known as the wireless body location network (WBAN). Human body verbal exchange (HBC), which uses the human frame because the communication medium, has these days emerged as an alternative to wireless media for conversation amongst these devices because of its low power requirement and more desirable safety residences. This alleviates key technological challenges: 1) electricity consumption, and 2) security, for such electricity-restricted battery-operated devices and may beautify their lifetime notably. One of the primary reasons for the electricity performance of HBC is due to the low loss channel supplied through the human frame, because of the conductance belongings of human tissue, compared to communique thru radio waves around the human frame. As a result, the entire know-how of the frequency characteristics of the human frame channel below special communication eventualities will permit the development of strength-efficient HBC primarily based on circuits and systems. Previous studies on HBC channel size have in most cases targeted intra-frame HBC, which characterizes the verbal exchange among two wearable devices worn by means of the identical character. There has been a huge variance in the measurement consequences reported in the literature mostly because of the experimental setup (low impedance size, vicinity of transmitter, receiver and many others.) and the excitation and termination modalities

### Used for
- safety
- termination
- security

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination
- security

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Fig. 4 in Geometric morphometric analysis and taxonomic revision of the Gzhelian (Late Pennsylvanian) conodont Idiognathodus simulator from North America

- **Website:** N/A
- **DOI:** 10.5281/zenodo.13264153
- **Status:** Unknown
- **Last updated:** 2024-08-28T13:09:06.694268+00:00

### Description
Fig. 4. Wireframe created by connecting landmarks chosen for the Idiognathodus simulator morphometric analysis. Numbers represent the landmark number designations used for the morphometric analysis: 1, ventral termination of the rostral adcarinal ridge; 2, dorsal termination of the carina; 3, ventral termination of the caudal adcarinal ridge; 4, rostral termination of the most ventral transverse ridge on the rostral side; 5, caudal termination of the most ventral transverse ridge on the rostral side; 6, rostral termination of the most ventral transverse ridge on the caudal side; 7, caudal termination of the most ventral transverse ridge on the caudal side; 8, rostral termination of the transverse ridge closest to the point of maximum curvature along the rostral platform margin on the rostral side. 9, caudal termination of the transverse ridge closest to the point of maximum curvature along the rostral platform margin on the rostral side; 10, rostral termination of the transverse ridge closest to the point of maximum curvature along the caudal platform margin on the caudal side; 11, caudal termination of the transverse ridge closest to the point of maximum curvature along the caudal platform margin on the caudal side; 12, rostral termination of the most dorsal transverse ridge on the rostral side; 13, caudal termination of the most dorsal transverse ridge on the rostral side; 14, rostral termination of the most dorsal transverse ridge on the caudal side; 15, caudal termination of the most dorsal transverse ridge on the caudal side; 16, dorsal tip of the element; 17, midpoint along the rostral adcarinal ridge; 18, midpoint along the caudal adcarinal ridge.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## A QSAT Benchmark Based on Vertex-Folkman Problems

- **Website:** N/A
- **DOI:** 10.5281/zenodo.3548977
- **Status:** Unknown
- **Last updated:** 2024-07-22T16:04:37.170449+00:00

### Description
The purpose of this project is to draw attention to a particular family of quantified Boolean formulas (QBFs) stemming from encodings of some vertex Folkman problems in extremal graph theory. We argue that this family of formulas is interesting for QSAT research because it is both conceptually simple and parametrized in a way that allows for a fine-grained diversity in the level of difficulty of its instances. Additionally, when coupled with symmetry breaking, the formulas in this family exhibit backbones (unique satisfying assignments) at the top-level existential variables. This benchmark is thus suitable for addressing questions regarding the connection between the existence of backbones and the hardness of QBFs.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## A comparative study of second trimester termination of pregnancy with mifepristone and misoprostol vs misoprostol alone in 50 cases

- **Website:** N/A
- **DOI:** 10.21303/2504-5679.2022.002726
- **Status:** Unknown
- **Last updated:** 2024-07-15T12:01:10.327763+00:00

### Description
The aim: To study the efficacy and safety of combined mifepristone and misoprostol used in second-trimester abortion(≥ 12 and ≤ 20 weeks) in comparison with only vaginal misoprostol.


Materials and methods: This study was a prospective comparative randomised clinical study in women attending hospitals in need of a second-trimester abortion, i.e., 12–20 weeks of pregnancy were taken up and divided as Group A – 50 women with mifeprisptone and misoprostol, Group B – 50 women with misoprostol alone Results were analysed according to age, parity, gestational age, average dose of misoprostol required for complete abortion, Induction abortion interval, completeness of abortion, side effects and mean days of hospital stay.


Results: Demographic details are comparable and insignificant in the comparison. The average dose of misoprostol (mcg) required for the completeness of abortion in group A is 596±28.28 mcg, and in group B, it is 1148±160.66 mcg (p<0.001) which is statistically significant. In the present study, the induction abortion interval is significantly less in group A compared to group B, with p<0.001. In addition, 10 out of 50 patients in group A aborted within 7 hours, whereas none in group B. Mean duration of hospital stay in group A is 24 hours. In group B, it is 34.82 hours which is statistically significant with a p-value of <0.001. 12 patients in group A and 26 in group B had side effects like nausea, vomiting, fever, headache and diarrhoea. 8 % of group A and 20 % of group B had a fever. These patients were treated with antipyretics. 6 % in group A and 14 % in group B had nausea and vomiting and were treated with antiemetics. 4 % in group A and 8 % in group B had diarrhoea and were treated with antimotility drugs. 6 % in group A and 10 % in group B had a headache; these patients were treated with NSAIDs.


Conclusions: The combination of mifepristone and misoprostol is a highly effective and safe method for second-trimester termination of pregnancy. The amount of misoprostol needed to accomplish the abortion, and the severity of the adverse effects are lower in the mifepristone-primed group than in the misoprostol-alone group. Since there are fewer difficulties, this approach can be employed in hospitals with high patient density.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## FIGURES 35–40 in A new species of Balaustium von Heyden, 1826 (Acari: Actinotrichida, Erythraeidae) from Spain

- **Website:** N/A
- **DOI:** 10.5281/zenodo.211654
- **Status:** Unknown
- **Last updated:** 2024-08-03T21:32:00.200194+00:00

### Description
FIGURES 35–40. Balaustium hernandezi sp. nov. (adult, female), SEM micrographs: 35. Eye (on the right) and urnula (on the left); 36. Dorsal opisthosomal setae; 37. Tarsus I termination; 38. Tarsus II termination; 39. Tarsus III termination; 40. Tarsus IV termination.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## jreeves3/qbf-definition-variable-movement-Artifact: Zenodo Archive

- **Website:** N/A
- **DOI:** 10.5281/zenodo.5733440
- **Status:** Unknown
- **Last updated:** 2021-11-29T13:48:45.166375+00:00

### Description
Archiving the artifact with Zenodo on release.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The moment of termination of corporate legal relations

- **Website:** N/A
- **DOI:** 10.21564/2414-990X.152.223330
- **Status:** Unknown
- **Last updated:** 2024-07-19T05:13:31.284753+00:00

### Description
The long-term nature of corporate legal relations necessitates the theoretical selection of certain moments of their emergence, change and termination. The update of the corporate legislation has necessitated a review of the established positions on the moment of termination of corporate legal relations, analysis and study of the legislation and resolution of problems that arise in connection with its application. The introduction of the institution of consent in corporate legal relations necessitated a scientific rethinking of certain aspects of the mechanism of termination of corporate legal relations. The article investigates the main scientific approaches to determining the moment of termination of corporate legal relations, analyzes the moment of termination of corporate legal relations depending on the grounds for their termination. Based on four main approaches to determining the moment of termination of corporate legal relations, the positions of scientists who adhere to them are studied, changes to the current corporate legislation are analyzed, inconsistencies regarding the moment of termination of corporate legal relations are revealed. The peculiarities of the moment of termination of corporate legal relations in case of alienation of a share (part of a share) in the authorized capital of the company, exclusion of a participant from the company, its withdrawal, withdrawal, recovery from the defendant (claim from his possession) to a share (part of the share) are analyzed. Peculiarities of state registration of changes in information about a legal entity in the aspect of determining the moment of termination of corporate legal relations are determined. A position has been formed regarding the application of a separate approach to determining the moment of termination of corporate legal relations on certain grounds for termination of corporate legal relations and suggested ways to resolve existing inconsistencies in corporate law regarding certain grounds for termination of corporate legal relations.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Profile of abortion seekers in the tertiary center of northern hills with review of medical termination of pregnancy act in India

- **Website:** N/A
- **DOI:** 10.15587/2519-4798.2021.249957
- **Status:** Unknown
- **Last updated:** 2024-07-17T12:21:15.195812+00:00

### Description
The aim of the present study was to investigate the socio-demographic and obstetric profile of pregnant women, seeking medical termination of pregnancy in accordance with the Medical Termination of Pregnancy (MTP) Act and the reasons for undergoing termination of pregnancy in the tertiary care center of the hilly region of Northern India and to further review the amendments in the Medical Termination of Pregnancy Act 1971 along with its future implications in legalizing abortions in India.

Materials and Methods: A registry-based retrospective study was carried out among pregnant women, attending the gynecologic outpatient department for termination of pregnancy at the tertiary care teaching hospital and the referral center for Himalayan foothills in Northern India. The records of women, seeking termination of pregnancy during a 1-year period between October 2020 and September 2021, were reviewed and information on their demographic and obstetric profile, reason for undergoing termination of pregnancy, and acceptance of contraception, following termination of pregnancy was recorded in the data sheet. The information obtained was analyzed using SPSS version 20 (IBM, Chicago, USA) for descriptive statistics.

Results: A total of 400 pregnant women underwent Medical Termination of Pregnancy between October 2020 and September 2021. 30.5 % (122/400) women between 26–30 years of age underwent termination of pregnancy, followed by 27.3 % women aged between 31–35 years. Social reasons for termination of pregnancy were more evident in women aged 26 years and above. 84.09 % pregnancies were terminated in the second trimester (>12 weeks) on eugenic ground, while 65.01 % pregnancies were terminated in the first trimester (6–12 weeks) on social grounds. Only 7.75 % (31/400) women opted for sterilization or family planning after MTP, out of which the majority opted for temporary methods of contraception.

Conclusion: We conclude from the results of the present study that women in the peak reproductive age (26–30 years) are more likely to seek pregnancy termination and this group of women needs to be the focus of contraceptive counseling and family planning services. Timely ultrasound scans by an expert sonologist may be a step forward towards lowering the rates of late pregnancy termination. There is a need to educate women to avail and use contraceptive methods in an effective manner and to make them aware of utilizing sterilization services, once they complete their families to avoid unwanted pregnancies.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Rho-dependent terminators and transcription termination

- **Website:** N/A
- **DOI:** 10.1099/mic.0.28982-0
- **Status:** Unknown
- **Last updated:** 2024-12-14T04:12:52.721076+00:00

### Description
Rho-dependent transcription terminators participate in sophisticated genetic regulatory mechanisms, in both bacteria and phages; they occur in regulatory regions preceding the coding sequences of genes and within coding sequences, as well as at the end of transcriptional units, to prevent readthrough transcription. Most Rho-dependent terminators have been found in enteric bacteria, but they also occur in Gram-positive bacteria and may be widespread among bacteria. Rho-dependent termination requires bothcis-acting elements, on the mRNA, andtrans-acting factors. The onlycis-acting element common to Rho-dependent terminators is richness in rC residues. Additional sequence elements have been observed at different Rho termination sites. These 'auxiliary elements' may assist in the termination process; they differ among terminators, their occurrence possibly depending on the function and sequence context of the terminator. Specific nucleotides required for termination have also been identified at Rho sites. Rho is the main factor required for termination; it is a ring-shaped hexameric protein with ATPase and helicase activities. NusG, NusA and NusB are additional factors participating in the termination process. Rho-dependent termination occurs by binding of Rho to ribosome-free mRNA, C-rich sites being good candidates for binding. Rho's ATPase is activated by Rho–mRNA binding, and provides the energy for Rho translocation along the mRNA; translocation requires sliding of the message into the central hole of the hexamer. When a polymerase pause site is encountered, the actual termination occurs, and the transcript is released by Rho's helicase activity. Many aspects of this process are still being studied. The isolation of mutants suppressing termination, site-directed mutagenesis ofcis-acting elements in Rho-dependent termination, and biochemistry, are and will be contributing to unravelling the still undefined aspects of the Rho termination machinery. Analysis of the more sophisticated regulatory mechanisms relying on Rho-dependent termination may be crucial in identifying new essential elements for termination.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Prove your Colorings: Formal Verification of Cache Coloring of Bao Hypervisor. Companion Artifact for the Paper Submitted to FASE 2025

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14616331
- **Status:** Unknown
- **Last updated:** 2025-01-17T17:01:29.921907+00:00

### Description
This artifact aims to support and reproduce the verification results of the paper  "Prove your Colorings: Formal Verification of Cache Coloring of Bao Hypervisor" by Axel Ferréol, Laurent Corbin and Nikolai Kosmatov, and should be cited as:
Axel Ferréol, Laurent Corbin and Nikolai Kosmatov. "Prove your Colorings: Formal Verification of Cache Coloring of Bao Hypervisor. Companion Artifact for the Paper Submitted to FASE 2025"
The artifact itself is available in the attached VM BaoVerifArtifact.ova. See the documentation in README.md in the folder /home/user/BaoVerifArtifact inside the VM.
For convenience of the readers and a faster access to files, the contents of the VM are also available in the attached ZIP. The ZIP is provided for information. The artifact should be preferably used with the attached VM BaoVerifArtifact.ova.The VM is running Ubuntu 24.04. The VM was tested with VirtualBox 7.1.2 on a host machine (with x86 architecture runnning Ubuntu 24.04). For information, the password of user "user" in the VM is "user". The default keyboard is French (press Super+Space, that is Windows button + Space, to change to English keyboard). 
Requirements for the VM:
- at least 4 CPU cores allocated for the VM; - at least 8 GB RAM allocated for the VM; - at least 25 GB free disk space before importing the VM.
See the included REQUIREMENTS.md file for more detail and the Disclaimer in README.md for possible reasons and situations when to increase allocated resources.
Hint: on some versions of host OS and VirtualBox, bugs or limited support prevent the use of VirtualBox or a correct termination of the VM start-up (the VM remains freezed on the loading screen). Changing the VM window size a couple of times can help to refresh the VM screen and get control on it. Otherwise check the known VirtualBox bugs or limitations.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Right to abortion & safe abortion will reduce maternal mortality

- **Website:** N/A
- **DOI:** 10.30574/gscbps.2022.21.1.0393
- **Status:** Unknown
- **Last updated:** 2024-07-15T20:34:16.919353+00:00

### Description
Abstract 
Recent report of the United Nations population fund’s state of the world population says that around 08 women die
every day in India because of unsafe abortion. There are many reasons behind the deaths such as taking abortion pills
without consulting doctor, abortion carried out by untrained personals, abortion in hospitals without facilities settings
etc. Married women have the right to abortion but what about the unmarried pregnant women; this case is one of the
major cause of unsafe abortion especially in our country India. Right to abortion simply means one can go for safe
abortion i.e. the abortion will be carried out by a trained doctor in a hospital approved for pregnancy termination having
facilities settings. Time to time amendments in Medical termination of Pregnancy act took place but no right provided
to unmarried. Supreme Court in its judgment on 29th September 2022 gave right to abortion to unmarried pregnant
women too up to 20 weeks from the date of gestation. This judgement came in a case that filed on July 2022 by 25 years
old pregnant women. The judgement is a revolution and save many lives of women because it will stop or reduce the
number of unsafe abortions.  The article discussed about the impact of this decision on women in near future, unsafe
abortion, medical abortion using medications, actions and adverse effects of medications used for abortion, medical
termination of pregnancy act 1971, amendment in act and effect of Supreme Court’s judgement on women’s health and
mortality.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The Medical Termination of Pregnancy (Amendment) Act 2021: A Boon or a Bane to Society

- **Website:** N/A
- **DOI:** 10.5281/zenodo.10213120
- **Status:** Unknown
- **Last updated:** 2024-07-10T17:19:38.727497+00:00

### Description
This paper has been published in Peer-reviewed International Journal "Remarking An Analisation"            URL : https://www.socialresearchfoundation.com/new/publish-journal.php?editID=7690Publisher : Social Research Foundation, Kanpur (SRF International)             Abstract :The Medical Termination of Pregnancy Act, 1971 is considered a major milestone of social legislations in India. However, 50 years of its application, it has failed to keep up with changing times, needs and advancements in technology. In this regard, The Medical Termination of Pregnancy (Amendment) Act, 2021 was a welcome step. Though the amendment made many necessary changes in the MTP Act. The aforementioned Amendment Act has failed to give any recognition to the right to abortion as a right to privacy of a pregnant woman. At no point of time during pregnancy can a pregnant woman seek abortion as per her choice. The Abortion law as such does not provide a pregnant woman right over her body making an essential human right like the right to privacy meaningless to a pregnant woman. The judiciary has time and again reiterated right to abortion as a right to privacy through different judgments. However, the legislature has time and again failed to give recognition to the same including the Medical Termination of Pregnancy (Amendment) Act 2021.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Synochoneura

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6242027
- **Status:** Unknown
- **Last updated:** 2024-12-10T02:10:56.137162+00:00

### Description
Key to species of Synochoneura based on the male genital characters1. Valva long and narrow, distinctly narrowed beyond middle, forming a neck; sacculus very long, exceeding termination of costa ................................................................................................................. S. ochriclivis- Valva short and broad, without distinctly narrowed neck; sacculus short, not reaching termination of costa......................................................................................................................................................................22. Distal part of valva slightly contracted; free termination of sacculus subquadrate; aedeagus slender........... .................................................................................................................................................. S. tapaishani- Distal part of valva distinctly contracted; free termination of sacculus dentate; aedeagus stout ................... ........................................................................................................................................ S. dentana sp. nov.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## HAK DAN KEWAJIBAN PEKERJA YANG DI RUMAHKAN AKIBAT DARI  PANDEMI COVID-19

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6562537
- **Status:** Unknown
- **Last updated:** 2024-07-16T18:06:46.171132+00:00

### Description
ABSTRACT

 

In the current pandemic, there are many problems that arise. Not only from the health aspect, but also from the employment aspect, human rights, etc. Moreover, in terms of rights, there are issues regarding the rights and obligations of workers who directly experience termination of employment (PHK). This is considered not in accordance with the rights and obligations of the workers, but due to the current pandemic conditions and leading to a crisis in all aspects of the field, the decision to lay off is the final decision made by the companies in order to avoid further losses in the company. Reducing employees is considered efficiency because it can help reduce expenses. There are so many companies that suppress HR behind this pandemic. There are layoffs, because there is no financial capability on the part of the company. It is felt, a pandemic situation like this is a responsibility and also a problem from all aspects. Not only about employees, but also the government, companies, all feel the impact of this pandemic.

Keywords: Pandemic, Workers, Termination.

 

ABSTRAK

 

Terhadap kondisi pendemi seperti saat ini sangat banyak problematika yang muncul. Tidak hanya dari aspek kesehatan, namun juga aspek ketenagakerjaan, hak asasi manusia, dll. Terlebih lagi dalam hak, adapun permasalahan atas hak dan kewajiban para pekerja yang secara langsung mendapati Pemutusan Hubungan Kerja (PHK). Hal ini dinilai tidak sesuai dengan hak dan kewajiban para pekerja, namun dikarenakan kondisi pandemi yang sepeeti ini dan berujung pada krisis disegala aspek bidang, maka keputusan PHK nenjadi keputusan akhir yang dilakukan oleh para perusahaan meningat agar tidak semakin rugi dalam perusahaan tersebut. Mengurangi karyawan adalah dianggap efisiensi karena dapat membantu mengurangi pengeluaran. Banyak sekali perusahaan yang menekan SDM di balik keadaan pandemi seperti ini. PHK ada, karena sudah tidak adanya kemampuan dari pihak perusahaan dari sisi keuangan. Dirasa, keadaan pandemi seperti imi adalah tanggungjawab dan juga masalah dari segala aspek. Tidak hanya tentang pegawai, namun juga pemerintahan, perusahaan, semua ikut merasakan dampak dari keadaan pandemi ini.

Kata Kunci: Pandemi, Pekerja, Pemutusan.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## HyperQB: A QBF-Based Bounded Model Checker for Hyperproperties

- **Website:** N/A
- **DOI:** 10.5281/zenodo.10048374
- **Status:** Unknown
- **Last updated:** 2023-10-28T04:42:52.570425+00:00

### Description
HyperQB is a push-button bounded model checker for hyperproperties. The inputs are model(s), in NuSMV syntax, a hyperproperty, in HyperLTL logic, and a finite bound k. HyperQB encodes the inputs as Boolean formulations and unroll up to k (additional bounded semantics can be given), and output either the given property is verified or falsified.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Termination patterns of Karenia brevis blooms in the eastern Gulf of Mexico

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7034923
- **Status:** Unknown
- **Last updated:** 2024-07-16T04:51:30.714211+00:00

### Description
The factors governing the initiation and development of K. brevis blooms in the eastern Gulf
of Mexico are fairly well understood, however the physical, chemical and biological factors
underlying bloom transport and termination are not. The Florida Fish and Wildlife Conservation
Commission’s HAB Monitoring database was analyzed from 1998 - 2021 for temporal trends in
bloom duration, initiation and termination and for repetitive spatial patterns in bloom termination.
A unimodal pattern in bloom initiation was observed, with the most frequent initiations in
September. Bloom termination was more variable, with the most frequent occurrences in April.
Four recurring patterns in bloom termination were identified during this period for southwest
Florida K. brevis blooms: 1) coastal transport south to the Florida Keys then west into the
Gulf of Mexico, 2) transport to the Florida Panhandle with subsequent termination in place,
or 3) via coastal transport west to Alabama, and 4) termination in place in southwest Florida.
These patterns suggest that consistent physical, chemical and biological drivers underlie the
termination stages of K. brevis blooms, and that identification of these drivers may provide
useful management tools for bloom prediction and monitoring.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The Termination— Ensis

- **Website:** N/A
- **DOI:** 10.1017/s0009840x00194764
- **Status:** Unknown
- **Last updated:** 2024-08-01T16:08:30.905015+00:00

### Description
n/a

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## AtrialFibrillation

- **Website:** N/A
- **DOI:** 10.13026/C2CC7Z
- **Status:** Unknown
- **Last updated:** 2024-03-22T09:31:54.399699+00:00

### Description
This is a physionet dataset of two-channel ECG recordings has been created from data used in the Computers in Cardiology Challenge 2004, an open competition with the goal of developing automated methods for predicting spontaneous termination of atrial fibrillation (AF).
The raw instances were 5 second segments of atrial fibrillation, containing two ECG signals, each sampled at 128 samples per second. The class labels are: n, s and t.

class n is described as a non termination artiral fibrilation(that is, it did not terminate for at least one hour after the original recording of the data).
class s is described as an atrial fibrilation that self terminates at least one minute after the recording process.
class t is described as terminating immediately, that is within one second of the recording ending.

This is a pre-processed version of the dataset saved in numpy format. The original dataset is obtained from here.
The data are 3-dimensional arrays of shape [n_samples, time_steps, n_variables]. The data can be loaded as follows:
loaded_data = np.load("AF.npz")
Xtr = loaded_data['Xtr'] # Training data of shape (4823, 45, 2)
Ytr = loaded_data['Ytr'] # Training labels of shape (4823, 1)
Xte = loaded_data['Xte'] # Test data of shape (185, 45, 2)
Yte = loaded_data['Yte'] # Test labels of shape (185, 1)

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## [ ATVA24 Artifact ] HyperQB: A QBF-Based Bounded Model Checker for Hyperproperties

- **Website:** N/A
- **DOI:** 10.5281/zenodo.11282197
- **Status:** Unknown
- **Last updated:** 2024-05-24T16:08:35.288296+00:00

### Description
Artifact for ATVA 2024, paper 80: HyperQB: A QBF-Based Bounded Model Checker for Hyperproperties

### Used for
(none)

### Input formats
- QBF

### Supported languages
(none)

### Supported inputs
- QBF

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Formal Verification of PKCS#1 Signature Parser using Frama-C. Companion Artifact for the Paper Submitted to iFM 2025

- **Website:** N/A
- **DOI:** 10.5281/zenodo.16919839
- **Status:** Unknown
- **Last updated:** 2025-09-03T08:12:54.971642+00:00

### Description
This artifact aims to support and reproduce the verification results of the paper  "Formal Verification of PKCS#1 Signature Parser using Frama-C" by Martin Hána, Nikolai Kosmatov, Virgile Prevosto and Julien Signoles, accepted for publication at iFM 2025, and should be cited as:
Martin Hána, Nikolai Kosmatov, Virgile Prevosto and Julien Signoles. "Formal Verification of PKCS#1 Signature Parser using Frama-C. Companion Artifact for the Paper Submitted to iFM 2025".  Zenodo. https://doi.org/10.5281/zenodo.16919839
The artifact itself is available in the attached VM PKCS1ParserProof.ova. See the documentation in README.md in the folder /home/user/PKCS1ParserProof/ inside the VM. In the provided VM, all tools have already been installed. 
The VM is running Ubuntu 24.04. The VM was tested with VirtualBox 7.0.14. For information, the password of user "user" in the VM is "user".  
For convenience of the readers and a faster access to files, the contents of the VM are also available in the attached ZIP. The ZIP is provided for information. The artifact should be preferably used with the attached VM PKCS1ParserProof.ova.Requirements for the VM:
- at least 4 CPU cores allocated for the VM; - at least 8 GB RAM allocated for the VM; - at least 25 GB free disk space before importing the VM.
See the included REQUIREMENTS.md file for more detail and the Disclaimer in README.md for possible reasons and situations when to increase allocated resources.
See the included LICENSE.md file for the licenses of different components. 
Hint: on some versions of host OS and VirtualBox, bugs or limited support prevent the use of VirtualBox or a correct termination of the VM start-up (the VM remains freezed on the loading screen). Changing the VM window size a couple of times can help to refresh the VM screen and get control on it. Otherwise check the known VirtualBox bugs or limitations. In particular, there are known compatibility issues for VirtualBox on ARM processors at the time of writing.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Juridical Review of Unilateral Termination of Employment by PT Indosat TBK during the Covid-19 Pandemic

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6416911
- **Status:** Unknown
- **Last updated:** 2024-07-16T22:50:41.717470+00:00

### Description
This research examined from a legal perspective regarding the unilateral termination of employment by PT Indosat Tbk, during the Covid-19 Pandemic. Two main issues were discussed in this study, the first was the chronology of unilateral termination carried out by PT Indosat Tbk to its employees during the Covid-19 pandemic, and analyzing the legal termination procedural during the Covid-19 Pandemic. This study used a normative juridical research method using secondary legal data. Based on the results of the study, it was known that the chronology of layoffs was carried out by PT. Indosat, Tbk to its workers during the Covid-19 pandemic was unilateral. Meanwhile, the legal termination procedure during the Covid-19 pandemic must go through the stages of negotiations between the employers, in this case, PT. Indosat, Tbk with employees represented by existing labor associations. In its implementation carried out, PT. Indosat, Tbk did not carry out negotiations before carrying out simultaneous termination. In connection with the above, the employer should negotiate first before implementing efficiency by doing the termination of employment (PHK).

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## FastForward for Termination

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7927876
- **Status:** Unknown
- **Last updated:** 2023-05-13T02:28:19.585441+00:00

### Description
Reproducible outcomes from the CAV paper "Fast Termination and Workflow Nets" by Piotr Hofman, Filip Mazowiecki and Philip Offtermatt.

 

The artifact contains implementations of several procedures related for fast termination in workflow nets, such as deciding whether a workflow net is terminating fast, and computing more fine-grained constants related to termination. The implementation is written as an extension to FastForward, a tool for decision and optimization procedures on Petri nets.

 

This artifact includes a virtual machine image, which is equipped with the source code of the artifact, a benchmark suite of workflow nets, and instructions on how to reproduce the experiments from our paper.

You can open the VM image e.g. with Virtualbox.

 

A reviewer reported issues with unzipping the zip file, obtaining the following error message when running ´unzip´:

Archive:  FastForwardForTermination.zip?download=1
warning [FastForwardForTermination.zip?download=1]:  5447050078 extra bytes at beginning or within zipfile
  (attempting to process anyway)
error [FastForwardForTermination.zip?download=1]:  start of central directory not found;
  zipfile corrupt.
  (please check that you have transferred or created the zipfile in the
  appropriate BINARY mode and that you have compiled UnZip properly)

1 archive had fatal errors.

A workaround to this problem is to run

` zip -FF -fz FastForwardForTermination.zip -O FastForwardForTermination.fixed.zip`,

then `unzip FastForwardForTermination.fixed.zip`

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
- SMT solving

### External tools
- Z3

### Examples
(none)

### References
(none)


---

## PBFD and PDFD: Formally Defined and Verified Methodologies and Empirical  Evaluation for Scalable Full-Stack Software Engineering

- **Website:** N/A
- **DOI:** 10.5281/zenodo.16883985
- **Status:** Unknown
- **Last updated:** 2025-08-17T02:55:56.424272+00:00

### Description
This paper introduces Primary Breadth-First Development (PBFD) and Primary Depth-First Development (PDFD), two formally defined and verified methodologies for scalable, industrial-grade full-stack software engineering. These approaches bridge a longstanding gap between formal methods and real-world development practice by enforcing structural correctness through graph-theoretic modeling. Unlike prior graph-based approaches, PBFD and PDFD operate over layered directed graphs and are formalized using unified state machines and Communicating Sequential Processes (CSP) to ensure critical properties, including bounded-refinement termination and structural completeness.
To coordinate hierarchical data at scale, we propose Three-Level Encapsulation (TLE)—a novel, bitmask-based encoding scheme that delivers provably constant-time updates. TLE’s formal guarantees underpin PBFD’s industrial-scale performance and scalability.
PBFD was empirically validated through an eight-year enterprise deployment, demonstrating over 20× faster development than Salesforce OmniScript and 7–8× faster query performance compared to conventional relational models. Additionally, both methodologies are supported by open-source MVPs, with PDFD’s implementation conclusively demonstrating its correctness-first design principles.
Together, PBFD and PDFD establish a reproducible, transparent framework that integrates formal verification into practical software development. All formal specifications, MVPs, and datasets are publicly available to foster academic research and industrial-grade adoption.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## CAV'25: Non-Termination Proving: 100 Million LoC and Beyond (Pulse Infinite Artifact)

- **Website:** N/A
- **DOI:** 10.5281/zenodo.15314312
- **Status:** Unknown
- **Last updated:** 2025-05-01T04:57:12.231376+00:00

### Description
This URL is intended to track the CAV'25 Artifact for paper: Non Termination Proving: 100 Million LoC and Beyond

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Artifact for the intermediate report "Modular termination verification with a higher-order concurrent separation logic" (December 2022) by Justus Fasse and Bart Jacobs

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7585369
- **Status:** Unknown
- **Last updated:** 2023-01-30T14:26:49.116100+00:00

### Description
# Artifact for the intermediate report "Modular termination verification with a higher-order concurrent separation logic" (December 2022) by Justus Fasse and Bart Jacobs

The file contains Coq theories built on top of Iris 4.0.

To facilitate comparison with the original Iris/HeapLang development, from which this artifact is derived, the source code is provided as a git bundle.

## How to build

Unpacking the git bundle
- `git clone artifact.bundle`
- `cd artifact`
- You should now already be on the `HeapLangLt` branch

To build
- `opam repo add coq-released https://coq.inria.fr/opam/released`
- `opam pin add coq-iris 4.0.0`
- `dune build`

## Directory structure

The rough directory structure of the development is described next. A precise list of changes can be obtained via git's diff mechanism.

1. The directory `modular_termination/` which defines the global ghost resource tracking the stock of call permissions, an instance of the Auth(Multiset) camera.
The Auth(Multiset) camera is reused in the proof of the concurrent stack with helping.

  - `auth_gmultiset.v` constructs the general Auth(Multiset) camera construction with some helper lemmas
  - `call_permissions.v` defines the global ghost resource used to reason about HeapLang<'s stock of call permissions

2. `iris_heap_lang/` provides an adapted version of Iris 4.0's HeapLang that defines HeapLang<.

  - `lang.v` defines the extended syntax and semantics of HeapLang<
  - `iris_heap_lang/primitive_laws.v` contains the `wp_burn` lemma
  - `iris_heap_lang/termination.v` gives the definitions and proofs that a HeapLang< program with "enough burns" (defined in the same file) cannot have infinite executions

3. `concurrent-stack-with-helping` contains the code for the case study of a concurrent stack with helping with a HoCAP-style specification. In general both the original code and our adaptions are present. In those cases, the definition with the prime (e.g. `concurrent_stack` vs. `concurrent_stack'`) is the version adapted for termination verification.

  - `specs.v` defines the HoCAP-style specification for concurrent stacks
  - `concurrent_stack4.v` gives an implementation satisfying the extended specification. The main theorems of the example are `push'_works` (`push'` corresponds to `push_inner` in the report), `push_outer_works` (`push_outer` corresponds to `push` in the report) and finally the proofs that the implementation satisfies the specification: `spec'`.
  - `client.v` defines a simple client of the specification. It creates a concurrent stack and pushes 42 twice to it, once in a forked off thread and once in the original thread.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Fig. 4 in Fig. 4 in Responses of Phyllostomid Bats to Traditional Agriculture in Neotropical Montane Forests of Southern Mexico.

- **Website:** N/A
- **DOI:** 10.5281/zenodo.12820996
- **Status:** Unknown
- **Last updated:** 2024-08-28T17:43:16.760428+00:00

### Description
Fig. 4. (a) Illustration of 17 landmarks on the Otolithes sp. 1: tip of snout, 2: termination of maxilla, 3: ventral margin of interopercle, 4: anterior margin of eye orbit, 5: posterior margin of eye orbit, 6: dorsal termination of cranium, 7: origin of lateral line, 8: origin of pectoral fin, 9: origin of pelvic fin, 10: anterior insertion of spinous dorsal fin, 11: origin of soft dorsal fin, 12: origin of anal fin; 13: termination of anal fin, 14: termination of second dorsal fin, 15: insertion of dorsal-most caudal fin ray, 16: termination of lateral line, and 17: insertion of ventral-most caudal fin ray. Procrustes superimposition showing the pair-wise differences in shapes between (b) Western Arabian Gulf group (WA) vs. West Indian Ocean II group, and (c) West Indian Ocean II group type A vs. B. Arrows indicate the difference vector, which is amplified four times for clarity.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## R data objects for the HumanDEU package

- **Website:** N/A
- **DOI:** 10.5281/zenodo.2583270
- **Status:** Unknown
- **Last updated:** 2020-01-24T19:25:04.332673+00:00

### Description
This submission contains several R data objects that are part of the R package HumanDEU available through Github (https://github.com/areyesq89/HumanTissuesDEU). The objects correspond to processed data needed to reproduce the statistics, tables and figures presented in the manuscript:

A Reyes and W Huber. Alternative start and termination sites of transcription drive most transcript isoform differences across human tissues. Nucleic Acids Research, 2017. doi: https://www.doi.org/10.1093/nar/gkx1165

For more details, please visit the Github repository.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Reproduction Package for FSE 2025 Submission `A Modular Program-Transformation Framework for Reducing Specifications to Reachability'

- **Website:** N/A
- **DOI:** 10.5281/zenodo.13757310
- **Status:** Unknown
- **Last updated:** 2024-09-30T08:27:03.658175+00:00

### Description
This is the Artifact for the paper “A Modular Program-Transformation Framework for Reducing Specifications to Reachability” which has been submitted to FSE 2025.
The FSE article presents a program transformation framework with the goal of verifying different properties with of-the-shelf reachability analyzers. The transformations in a framework is based on instrumentation automata, inspired by the BLAST query language. In our initial study, we support three important concrete specifications for C programs: termination, no-overflow, and memory cleanup. This artifact can be used to reproduce the experiments presented in the paper. We demonstrate the effectiveness and efficiency of our transformations by comparing verifiers that support the specifications natively with verifiers for reachability applied to the transformed programs. The results are very promising: Our transformations can extend existing verifiers to be effective on specifications that they do not support natively, and that the efficiency is often similar to verifiers that natively support the considered specifications.
The artifact consists of Makefile that can be used to download all the revisions of the tools used in the evaluation. Moreover, it downloads the transformation framework from git repository and sets it to the right version and branch. Further, it contains benchmarking definitions used by BenchExec to execute the experiments and processing scripts of the results that were used to generate the tables. Folder figures-generation/results-FSE2025 contains all the data that we computed.
Contents
The artifact contains the following items: - README.{html,md}: this documentation - Makefile: makefile containing all the commands for getting the source code of all the tools and our framework - benchmark-defs/: definitions needed for BenchExec to run the experiments - figures-generation/: folder containing all the processing scripts for the results and the results form our experiments - tasks/: definitions for our selected subsets of tasks that can be used to run the tool
TL;DR

Setup variables in your shell environment to one of these:

If you have access to a BenchCloud instance use source benchmark-utils/config_vcloud.sh, adapting it correspondingly to your server
To execute on your local system use source benchmark-utils/config.sh. You may want to adapt the amount of processes running in parallel by adjusting the number of processes in -N 2.


Select the tasks which you would like to use:

make tasks-benchmark: to setup all tasks used in the experiments in the paper
make tasks-subset: to setup tasks to run a representative subset of tasks for the experiments in the paper
make tasks-test: to setup a few tasks to test the functionality of the artifact


If not executing inside the artifact VM, you need to install everything using make setup-all. This may take a while and you may want to set a symlink to your SV-Benchmarks copy if available.
If you wish to only get the code of the transformation framework, run make specification-transformation.
Execute the verification tasks on the original properties using make experiments-original-property
Transform the properties to reachability using make transform-all-properties
Execute the verification tasks where the original property has been encoded as a reachability property using make experiments-transformed
Analyze the results to get the tables and plots from the paper using make process-results

Running BenchExec
When running BenchExec some directories need to be given as overlay, hidden and full access. Which ones are what is given in config.sh. If not using the artifact VM, you should adjust them to your own paths.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## European Autonomous Flight Termination Systems Based in Smart Avionics

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14161129
- **Status:** Unknown
- **Last updated:** 2025-04-11T08:36:02.190806+00:00

### Description
Operating a launcher is not exempt from risks. Even if we are talking about a reliable and tested system, the launchers need to operate in a very harsh environment. Thus, any issue can cause a failure and the loss of the control on the system. During the ascent phase, any failure implies risks to human lives since it would be a huge uncontrolled vehicle full of flammable fuel. Therefore, the launchers are tracked and monitored during the ascent phase, and in case any issue is detected, the launcher needs to immediately terminate (typically exploding).
A traditional flight termination architecture ensures independency from the vehicle functional chain using a radar network with human involvement in the decision-making process. This means: (i) considerable budget share for infrastructure and operations, (ii) limited flexibility (radar network needed), (iii) vehicle monitoring restricted to LOS conditions and (iv) delay inherent to communications and human reaction.
The autonomous flight termination systems (AFTS) determine the safety of the flight by processing different tracking inputs and comparing current estimated state to flight rules (also known as mission rules), defined by the user during flight missionization phase. By processing the mission rules directly on-board, the reaction time is reduced, and the telemetry downlink is no longer required.
Within Europe, there is no clear standard on the design nor operation of an AFTS. The critical part of this type of standards is related to managing the idiosyncrasy of the flight regulation in each country, making it difficult to have a common standard in Europe. The solution proposed is to have a highly configurable unit, in which the range safety officer could even include proprietary software for the termination logic, thus adapting to each specific local flight regulation without the need to perform any factory customization.
The paper describes the general problem and the proposed solution for a European Autonomous Flight Termination System highly configurable by the user, which make is suitable for a broad range of launchers and countries. Sener is developing an AFTU demonstrator in the frame of the RD EC Horizon Europe programme.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Empirical Research on the Issues of Termination of Employee Relationships Post Pandemi Covid-19. Urgency of the Role of Work Motivation and Employee Trust: Evidence from Indonesia

- **Website:** N/A
- **DOI:** 10.5281/zenodo.8167440
- **Status:** Unknown
- **Last updated:** 2024-07-11T16:45:18.656164+00:00

### Description
The purpose of this study was to determine the effect of Work Motivation and Employee Trust on Termination Anxiety Issues post the COVID-19 Pandemic. This research is classified as Explanatory Research with a quantitative approach. The sample used was 90 employees of PT.Marinal Indo Prima with purposive sampling technique. The type of data used is primary data, namely data collection using a questionnaire. Analysis of the data used is Multiple Linear Regression with SPSS. The results of this study indicate that work motivation has a negative effect on Termination Anxiety Issues. Likewise, Employee Trust has a negative effect on Termination Anxiety Issues. Simultaneously Work Motivation and Employee Trust have an effect on Termination Anxiety Issues.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Further Materials (Additional Slides, Write-ups, Results, etc.) for Fanoos: Multi-Resolution, Multi-Strength, Interactive XAI System

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6614276
- **Status:** Unknown
- **Last updated:** 2022-06-04T23:39:22.760597+00:00

### Description
This upload contains a tarred and compressed copy of the slides, documents, git-history, and other material available at https://github.com/DBay-ani/FanoosFurtherMaterials as of minute 54 hour 22 day 4 month 6 year 2022 UTC.

See the following paper for a description:

    @inproceedings{DBLP:conf/vmcai/BayaniM22,
      author    = {David Bayani and Stefan Mitsch},
      editor    = {Bernd Finkbeiner and
                   Thomas Wies},
      title     = {Fanoos: Multi-resolution, Multi-strength, Interactive Explanations for Learned Systems},
      booktitle = {Verification, Model Checking, and Abstract Interpretation - 23rd International Conference, {VMCAI} 2022, Philadelphia, PA, USA, January 16-18, 2022, Proceedings},
      series    = {Lecture Notes in Computer Science},
      volume    = {13182},
      pages     = {43--68},
      publisher = {Springer},
      year      = {2022},
      url       = {https://doi.org/10.1007/978-3-030-94583-1\_3},
      doi       = {10.1007/978-3-030-94583-1\_3},
      timestamp = {Fri, 21 Jan 2022 22:02:46 +0100},
      biburl    = {https://dblp.org/rec/conf/vmcai/BayaniM22.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }

or see the extended write-up at:

    @article{bayani2020fanoos,
      title={Fanoos: Multi-Resolution, Multi-Strength, Interactive Explanations for Learned Systems},
      author={Bayani, David and Mitsch, Stefan},
      journal={arXiv preprint arXiv:2006.12453},
      year={2020},
      url={https://arxiv.org/abs/2006.12453}
    }

This upload is related to the code available on the following Zenodo item:

    @software{david_bayani_2021_5513079,
      author       = {David Bayani},
      title        = {{Code for the Fanoos Multi-Resolution, Multi-Strength, Interactive XAI System}},
      month        = mar,
      year         = 2021,
      publisher    = {Zenodo},
      doi          = {10.5281/zenodo.5513079},
      url          = {https://doi.org/10.5281/zenodo.5513079}
    }

We note that this upload ("Further Material for Fanoos [...]"), in contrast to the material cited immediately above, contains additional documents, results, slides, etc., related to Fanoos, as opposed to its source code.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
- model checking
- abstract interpretation

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Influence of Cover Crop Termination on Ground Dwelling Arthropods in Organic Vegetable Systems

- **Website:** N/A
- **DOI:** 10.5281/zenodo.14717947
- **Status:** Unknown
- **Last updated:** 2025-01-22T11:04:39.755132+00:00

### Description
A key aspect in cover crop management is termination before the cash crop is planted.The aim of this study was to assess the effects of termination methods on ground-dwellingarthropods. The conventional mechanical termination method—i.e., green manuring by means of adisc harrow—was compared to flattening using a roller crimper. Two different crop systems wereinvestigated for two growing seasons; cauliflower was grown in autumn after the termination of amixture of cowpea, pearl millet, and radish, and tomato was cropped in spring and summer after thetermination of a mixture of barley and vetch. Ground beetles (Coleoptera: Carabidae), rove beetles(Coleoptera: Staphylinidae), and spiders (Araneae) were sampled by means of standard pitfalltraps throughout the growing season of both cash crops. The roller crimper increased the overallabundance of ground beetles in the first growing season of both cash crops, whereas in the secondyear, no significant effect could be detected. Rove beetles were more abundant in plots where thecover crops were terminated by the roller crimper. Finally, green manuring increased the abundanceof spiders, especially on the first sampling date after cover crop termination. Albeit different taxashowed different responses, the termination of cover crops by a roller crimper generally increased theabundance of ground dwelling arthropods. Given that most of the sampled species were generalistpredators, their increased abundance could possibly improve biological control

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Mulu Borneo stalagmite SC02 d18O and d13C 19.5-10.7 ky BP

- **Website:** N/A
- **DOI:** 10.5281/zenodo.6026615
- **Status:** Unknown
- **Last updated:** 2022-02-24T17:47:14.781260+00:00

### Description
Here are presented Mulu, Borneo (4°6’N, 114°53’E) Secret Cave stalagmite SC02 d18O and d13C values over Termination 1, published in Buckingham et al. (accepted). U-Th ages were calculated using the initial detrital 230Th/232Th value of 111 ± 41 ppm. A Matlab Monte Carlo script was used to calculated the absolute age and age errors associated with each U-Th sample. The Poisson-process deposition model feature in OxCal(v4.4) was used to interpolate between the eighteen U/Th ages to produce an age model. This study reports a d18O and d13C record for the portion of SC02 104.1 to 182.4 mm distance from top of stalagmite. The d18O record spans the full deglaciation, and reveals distinct d18O variations connected with the Bølling-Allerød onset and the Younger Dryas event.

### Used for
- termination

### Input formats
(none)

### Supported languages
- MATLAB

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Preliminary Results from an AFTU Prototype Based on Smart Avionics

- **Website:** N/A
- **DOI:** 10.5281/zenodo.15188152
- **Status:** Unknown
- **Last updated:** 2025-04-11T08:27:47.233149+00:00

### Description
This paper presents the development and testing of an Autonomous Flight Termination Unit (AFTU) within the SAFEST project framework. Traditional flight termination systems rely heavily on ground-based infrastructure, which limits flexibility, incurs high costs, and introduces delays due to human decision-making. The proposed AFTU leverages advances in GNSS technology, onboard computational capabilities, and avionics software platforms to enable real-time, autonomous termination decisions. The unit is highly configurable, allowing range safety officers to define mission-specific rules and integrate proprietary software to meet varying national regulations across Europe.
The paper focuses on the initial prototype's test campaign that Sener is developing in the frame of the RD EC Horizon Europe programme., detailing the system architecture, test setup, and performance results. It also outlines the roadmap toward flight qualification, emphasizing the system’s adaptability for different launchers and regulatory environments.

### Used for
- safety
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- safety
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## FIGURE 6 in New species of Grubeulepis Pettibone, 1969 (Eulepethidae, Annelida) from northern Brazil

- **Website:** N/A
- **DOI:** 10.5281/zenodo.1301877
- **Status:** Unknown
- **Last updated:** 2024-08-02T05:39:03.893879+00:00

### Description
FIGURE 6. Grubeulepis serrata sp. nov. A, Spiny notochaetae; B, Spiny notochaeta with spatulated-shaped termination; C, Notochaeta with spoon-shaped termination; D, Notochaetae with denticles. Scales: A–C = 0.03 mm; D = 0.06 mm.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Code for the Fanoos Multi-Resolution, Multi-Strength, Interactive XAI System

- **Website:** N/A
- **DOI:** 10.5281/zenodo.5513079
- **Status:** Unknown
- **Last updated:** 2022-02-14T21:31:34.559742+00:00

### Description
This upload contains a tarred and compressed copy of the code and git-history available at https://github.com/DBay-ani/Fanoos as of hour 3 day 16 month 5 year 2021 UTC.

See the following paper for a description:

    @inproceedings{DBLP:conf/vmcai/BayaniM22,
      author    = {David Bayani and Stefan Mitsch},
      editor    = {Bernd Finkbeiner and
                   Thomas Wies},
      title     = {Fanoos: Multi-resolution, Multi-strength, Interactive Explanations for Learned Systems},
      booktitle = {Verification, Model Checking, and Abstract Interpretation - 23rd International Conference, {VMCAI} 2022, Philadelphia, PA, USA, January 16-18, 2022, Proceedings},
      series    = {Lecture Notes in Computer Science},
      volume    = {13182},
      pages     = {43--68},
      publisher = {Springer},
      year      = {2022},
      url       = {https://doi.org/10.1007/978-3-030-94583-1\_3},
      doi       = {10.1007/978-3-030-94583-1\_3},
      timestamp = {Fri, 21 Jan 2022 22:02:46 +0100},
      biburl    = {https://dblp.org/rec/conf/vmcai/BayaniM22.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }

or see the extended write-up at:

    @article{bayani2020fanoos,
      title={Fanoos: Multi-Resolution, Multi-Strength, Interactive Explanations for Learned Systems},
      author={Bayani, David and Mitsch, Stefan},
      journal={arXiv preprint arXiv:2006.12453},
      year={2020},
      url={https://arxiv.org/abs/2006.12453}
    }

This upload is related to the additional written materials available on the
following Zenodo item:

    @misc{david_bayani_2022_6069468,
      author       = {David Bayani},
      title        = {{Further Materials (Additional Slides, Write-ups, Results, etc.) for Fanoos: Multi-Resolution, Multi-Strength, Interactive XAI System}},
      month        = feb,
      year         = 2022,
      publisher    = {Zenodo},
      doi          = {10.5281/zenodo.6069468},
      url          = {https://doi.org/10.5281/zenodo.6069468}
    }

We note that this upload ("Code for Fanoos [...]"), in contrast to the material
cited immediately above, contains source related to Fanoos, as opposed to
additional write-up, slides, etc.

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
- model checking
- abstract interpretation

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Reproduction Package for STTT Submission `Cooperative Verification: A Literature Review'

- **Website:** N/A
- **DOI:** 10.5281/zenodo.7838608
- **Status:** Unknown
- **Last updated:** 2023-04-29T14:26:38.858367+00:00

### Description
This artifact contains the aggregated data used for the article “Cooperative Verification: A Literature Review”.

The artifact consists of the following data files:

|– stage-1_search-space.csv
|– stage-2-3-4_keyword-search_process-title-abstract.csv
|– review_sheet.csv

Search space for literature review

The file stage-1_search-space.csv contains metadata for the articles comprising the search space for our literature review. These data correspond to the output of Stage 1 in the methodology described in the paper.

Filtering process

The file stage-2-3-4_keyword-search_process-title-abstract.csv contains the data corresponding to the stages 2, 3, and 4 of the methodology described in the paper. It contains metadata for the articles that passed the filter of keyword-search, and the decisions based on reviewing titles and abstracts.

Review sheet

The file review_sheet.csv contains metadata for the articles we reviewed. It contains the information related to the application of our definition to the techniques presented in these articles, as well as the class assigned to the cooperative techniques.

Generating numbers

Following commands can be executed to reproduce the numbers used in our literature review.

# Change directory to the directory containing the CSV files of this artifact.

# Number of papers in our search space.
cat stage-1_search-space.csv | tail -n +2 | wc -l

# Number of papers after keyword search.
cat stage-2-3-4_keyword-search_process-title-abstract.csv | tail -n +2 | wc -l

# Number of papers that are excluded based on titles.
cut -f11 stage-2-3-4_keyword-search_process-title-abstract.csv | tail -n +2 | sort | uniq -c

# Number of papers that are excluded based on abstracts.
cut -f12 stage-2-3-4_keyword-search_process-title-abstract.csv | tail -n +2 | sort | uniq -c

# Number of papers in different combination classes.
cut -f8 review_sheet.csv | tail -n +2 | sort | uniq -c

### Used for
(none)

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## A termination analyzer for Java bytecode based on path-length

- **Website:** N/A
- **DOI:** 10.1145/1709093.1709095
- **Status:** Unknown
- **Last updated:** 2024-12-09T18:43:39.384741+00:00

### Description
It is important to prove that supposedly terminating programs actually terminate, particularly if those programs must be run on critical systems or downloaded into a client such as a mobile phone. Although termination of computer programs is generally undecidable, it is possible and useful to prove termination of a large, nontrivial subset of the terminating programs. In this article, we present our termination analyzer for sequential Java bytecode, based on a program property called
            path-length
            . We describe the analyses which are needed before the path-length can be computed such as sharing, cyclicity, and aliasing. Then we formally define the path-length analysis and prove it correct with respect to a reference denotational semantics of the bytecode. We show that a constraint logic program
            P
            
              CLP
            
            can be built from the result of the path-length analysis of a Java bytecode program
            P
            and formally prove that if
            P
            
              CLP
            
            terminates, then
            P
            also terminates. Hence a termination prover for constraint logic programs can be applied to prove the termination of
            P
            . We conclude with some discussion of the possibilities and limitations of our approach. Ours is the first existing termination analyzer for Java bytecode dealing with any kind of data structures dynamically allocated on the heap and which does not require any help or annotation on the part of the user.

### Used for
- termination

### Input formats
(none)

### Supported languages
- Java

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Figure 5 from: Ulmer JM, Mikó I, Deans AR, Krogmann L (2021) The Waterston's evaporatorium of Ceraphronidae (Ceraphronoidea, Hymenoptera): A morphological barcode to a cryptic taxon. Journal of Hymenoptera Research 85: 29-56. https://doi.org/10.3897/jhr.85.67165

- **Website:** N/A
- **DOI:** 10.3897/jhr.85.67165.figure5
- **Status:** Unknown
- **Last updated:** 2024-07-17T19:32:26.346424+00:00

### Description
Figure 5 Dorsal vessel termination in Ceraphronoidea (CLSM) A dorsal vessel termination of Conostigmus sp. B dorsal vessel and abdominal pulsatory organ of Ceraphron sp. C abdominal pulsatory organ and evaporatorium in Aphanogmus sp.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Review of contractual obligations in the Civil Code of Ukraine

- **Website:** N/A
- **DOI:** 10.17533/udea.esde.v76n167a06
- **Status:** Unknown
- **Last updated:** 2024-07-22T18:35:04.543163+00:00

### Description
Breaching of contractual obligations may lead to certain negative consequences. Hence, this work analyzes the theoretical aspects of termination of contractual obligations in Ukraine’s civil law. The article aims to study the obligation termination mechanism by determining the legal framework for its functioning. The author focuses on one of the forms of contractual obligation termination, more specifically, the start of cancellation and deferred status of a legal transaction. Using normative and protective functions in legislation, the author plans to determine specifics of legal facts of normative compensatory nature. It is established, that the condition for cancellation of a legal transaction, can be a direct or reverse mechanism for the termination of contractual obligations. A condition for cancellation of a legal transaction can be applied to the whole transaction or to its separate parts.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Termination Resilience Static Analysis

- **Website:** N/A
- **DOI:** 10.5281/zenodo.17176433
- **Status:** Unknown
- **Last updated:** 2025-09-22T11:48:30.413091+00:00

### Description
FuncTion is a research prototype static analyzer designed for proving conditional termination resilience (and  termination and conditional CTL properties of C programs.
The tool automatically infers piecewise-defined ranking functions and sufficient preconditions by means of abstract interpretation.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
- abstract interpretation

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Benchmarks for program termination

- **Website:** N/A
- **DOI:** 10.5281/zenodo.13756495
- **Status:** Unknown
- **Last updated:** 2024-09-13T06:25:30.756838+00:00

### Description
Benchmarks for program termination

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Ensuring Termination in ESFP

- **Website:** N/A
- **DOI:** 10.3217/jucs-006-04-0474
- **Status:** Unknown
- **Last updated:** 2024-07-16T06:16:17.415034+00:00

### Description
In previous papers we have proposed an elementary discipline of strong functional programming (ESFP), in which all computations terminate. A key feature of the discipline is that we introduce a type distinction between data which is known to be finite, and codata which is (potentially) infinite. To ensure termination, recursion over data must be well-founded, and corecursion (the definition schema for codata) must be productive, and both of these restrictions must be enforced automatically by the compiler. In our previous work we used abstract interpretation to establish the productivity of corecursive definitions in an elementary strong functional language. We show here that similar ideas can be applied in the dual case to check whether recursive function definitions are strongly normalising. We thus exhibit a powerful termination analysis technique which we demonstrate can be extended to partial functions.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
- abstract interpretation

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Chorea, With Fatal Termination.

- **Website:** N/A
- **DOI:** 10.1016/s0140-6736(02)80667-5
- **Status:** Unknown
- **Last updated:** 2024-08-01T15:55:40.061286+00:00

### Description
n/a

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Data from: One phase of the dormancy developmental pathway is critical for the evolution of insect seasonality

- **Website:** N/A
- **DOI:** 10.5061/dryad.1vh94
- **Status:** Unknown
- **Last updated:** 2022-05-29T23:07:58.305204+00:00

### Description
Evolutionary change in the timing of dormancy enables animals and plants to adapt to changing seasonal environments and can result in ecological speciation. Despite its clear biological importance, the mechanisms underlying the evolution of dormancy timing in animals remain poorly understood because of a lack of anatomical landmarks to discern which phase of dormancy an individual is experiencing. Taking advantage of the nearly universal characteristic of metabolic suppression during insect dormancy (diapause), we use patterns of respiratory metabolism to document physiological landmarks of dormancy and test which of the distinct phases of the dormancy developmental pathway contribute to a month-long shift in diapause timing between a pair of incipient moth species. Here, we show that divergence in life cycle between the earlier-emerging E-strain and the later-emerging Z-strain of European corn borer (ECB) is clearly explained by a delay in the timing of the developmental transition from the diapause maintenance phase to the termination phase. Along with recent findings indicating that life-cycle differences between ECB strains stem from allelic variation at a single sex-linked locus, our results demonstrate how dramatic shifts in animal seasonality can result from simple developmental and genetic changes. Although characterizing the multiple phases of the diapause developmental programme in other locally adapted populations and species will undoubtedly yield surprises about the nature of animal dormancy, results in the ECB moth suggest that focusing on genetic variation in the timing of the dormancy termination phase may help explain how (or whether) organisms rapidly respond to global climate change, expand their ranges after accidental or managed introductions, undergo seasonal adaptation, or evolve into distinct species through allochronic isolation.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## The Spatial Constraint Requiring Organogenetic Termination: Supplemental to Haeckel and von Baer for Development and Evolution

- **Website:** N/A
- **DOI:** 10.59324/ejtas.2024.2(3).39
- **Status:** Unknown
- **Last updated:** 2024-06-03T11:37:33.697655+00:00

### Description
In this article, it is pointed out that the requirement for organogenetic termination is the new spatial constraint for animal development and heredity, based on that: (a) organogenesis manifests limitation in time and possession of termination, while infinite cell proliferation known as cancer is lethal; (b) the notable indeterminate growth in some fishes and a few outgrowing skin derivatives reversely demonstrates that termination is required for organogenesis inside the animal. In further, it is supplemented this new spatial constraint to Haeckel and von Baer for development and evolution. While not influencing the temporal and spatial reorganization of morphogenesis during evolution, it places restrictions on alteration of organogenetic mechanisms themselves, as that: (a) addition of new induction mechanism or elimination of termination mechanism would usually cause endless organogenesis, liable to become lethal; (b) addition of new termination mechanism or elimination of induction mechanism in evolution not be affected by this spatial constraint. Finally, it is identified this spatial constraint as partial convergence and partial difference with Haeckel’s recapitulation, and as restriction onto Baer’s tree. It is perspectives to use the method of mathematical probability and statistics to study the spatial constraint of development onto evolution in future.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Termination of rights in the mechanism of civil legal relations

- **Website:** N/A
- **DOI:** 10.5281/zenodo.4046883
- **Status:** Unknown
- **Last updated:** 2024-07-19T15:37:09.936684+00:00

### Description
The article aims to research the termination of rights in the mechanism of civil legal relations. The relevance of the work is expressed by the fact that the analysis of the reasons for termination of right is based on the analysis of legal facts that are realized in the process of formalization of some civil legal relations. The fol-lowing methods were used: analysis, synthesis, comparison, abstraction. The nov-elty of the study is determined by the fact that the authors of the article research the causes of termination of right and the possibility of implementing this process is universal and local legal systems. The authors consider each of the principles of termination of right as an opportunity to form a qualitatively new subject of re-search and development of the local legal system. The article analyzes the general grounds for termination of rights and suggests implementation measures with consideration of international law. The practical relevance of the study is determined by the fact that for the first time not only direct forms of restriction of rights and measures to terminate them were considered, but also recommendations were developed on the details of the matter in question.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Figure 5 from: Wisitrassameewong K, Park MS, Lee H, Ghosh A, Das K, Buyck B, Looney BP, Caboň M, Adamčík S, Kim C, Kim CS, Lim YW (2020) Taxonomic revision of Russula subsection Amoeninae from South Korea. MycoKeys 75: 1-29. https://doi.org/10.3897/mycokeys.75.53673

- **Website:** N/A
- **DOI:** 10.3897/mycokeys.75.53673.figure5
- **Status:** Unknown
- **Last updated:** 2024-07-19T13:37:54.465937+00:00

### Description
Figure 5 Microscopic features of Russula bella (SFC20170819-05) A basidia B basidiola C clavate marginal cells D hymenial cystidia on lamellae sides E subulate marginal cells F hyphal termination at pileus margin G hyphal termination at pileus centre. Scale bars: 10 µm.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Figure 6 from: Wisitrassameewong K, Park MS, Lee H, Ghosh A, Das K, Buyck B, Looney BP, Caboň M, Adamčík S, Kim C, Kim CS, Lim YW (2020) Taxonomic revision of Russula subsection Amoeninae from South Korea. MycoKeys 75: 1-29. https://doi.org/10.3897/mycokeys.75.53673

- **Website:** N/A
- **DOI:** 10.3897/mycokeys.75.53673.figure6
- **Status:** Unknown
- **Last updated:** 2024-07-19T13:37:54.266517+00:00

### Description
Figure 6 Microscopic features of Russula orientipurpurea (SFC20170725-37) A basidia B basidiola C clavate marginal cells D hymenial cystidia on lamellae sides E subulate marginal cells F hyphal termination at pileus margin G hyphal termination at pileus centre. Scale bars: 10 µm.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Figure 7 from: Wisitrassameewong K, Park MS, Lee H, Ghosh A, Das K, Buyck B, Looney BP, Caboň M, Adamčík S, Kim C, Kim CS, Lim YW (2020) Taxonomic revision of Russula subsection Amoeninae from South Korea. MycoKeys 75: 1-29. https://doi.org/10.3897/mycokeys.75.53673

- **Website:** N/A
- **DOI:** 10.3897/mycokeys.75.53673.figure7
- **Status:** Unknown
- **Last updated:** 2024-07-19T13:37:54.039550+00:00

### Description
Figure 7 Microscopic features of Russula sp. (SFC20160726-13) A basidia B basidiola C clavate marginal cells D hymenial cystidia on lamellae sides E subulate marginal cells F hyphal termination at pileus margin G hyphal termination at pileus centre. Scale bars: 10 µm.

### Used for
- termination

### Input formats
(none)

### Supported languages
- C

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## Soil N<sub>2</sub>O emissions after perennial legume termination in an alfalfa-wheat crop rotation system under Mediterranean conditions

- **Website:** N/A
- **DOI:** 10.4081/ija.2020.1613
- **Status:** Unknown
- **Last updated:** 2024-12-08T14:13:19.058501+00:00

### Description
Agricultural activities are potential sources of greenhouse gas (GHG) emissions, and nitrous oxide (N2O) is one of the most important non-carbon-dioxide GHGs. Perennial legumes such as alfalfa (Medicago sativa L.) have potential roles for reduction of soil GHG emissions as part of crop rotation systems. However, the implications of perennial legume termination by tillage and subsequent soil incorporation of the residues for reduced GHG emissions have been poorly examined in Mediterranean environments. With the aim to assess the magnitude of soil N2O emissions (important for the definition of mitigation strategies) after perennial legume termination in alfalfa-wheat crop rotation systems in a Mediterranean environment, we defined the hypothesis that alfalfa termination by tillage with incorporation of the crop residues will increase soil N2O emissions during the subsequent wheat season. To test this hypothesis, closed static chambers were used in a field–plot experiment, using a complete randomised block design with three replicates. Soil N2O emissions were monitored across 33 sampling dates from October 2017 to July 2018, as a comparison between an original 6-year-old alfalfa field ('continuous alfalfa') and alfalfa termination followed by wheat ('alfalfa+ wheat'). The soil N2O emission fluxes varied markedly across the treatments and throughout the monitoring period (from – 0.02±0.01 to 0.53±0.14 g N-N2O ha–1 h–1, and from 0.02±0.07 to 0.37±0.11 g N-N2O ha–1 h–1 for continuous alfalfa and alfalfa+wheat, respectively), generally following the changes in soil temperature. Several soil N2O emission peaks were recorded for both treatments, which mainly coincided with rainfall and with increased soil water content. In the 2 months following alfalfa termination, alfalfa+wheat showed higher cumulative weekly soil N2O emissions compared to continuous alfalfa. Following alfalfa termination for alfalfa+wheat, the increased cumulative weekly soil N2O emissions appeared to be due to asynchrony between nitrogen (N) released into the soil from mineralisation of the alfalfa residues and N uptake by the wheat. Despite these initial high soil N2O emissions for alfalfa+wheat, the seasonal cumulative soil N2O emissions were not significantly different (0.77±0.09 vs 0.85±0.18 kg N-N2O ha–1 for continuous alfalfa and alfalfa+wheat, respectively). These data suggest that legume perennial crop termination in alfalfa–wheat rotation systems does not lead to significant loss of N2O from the soil. The alfalfa termination by tillage performed in autumn might, on the one hand, have slowed the mineralisation process, and might, on the other hand, have synchronised the N release by the mineralised crop residues, with the N uptake by the wheat reducing the soil N2O emissions.
Highlights - Soil N2O emissions peak after alfalfa termination and rainfall. - Soil N2O emissions increase after spring alfalfa mowing. - Seasonal cumulative soil N2O emissions are similar for alfalfa and alfalfa followed by wheat. - Mitigation effects of perennial legume on soil N2O emissions are not lost after termination by tillage under alfalfa-wheat rotation.

### Used for
- termination

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
- termination

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---

## TCP-drought-termination-v1.0.0

- **Website:** N/A
- **DOI:** 10.5281/zenodo.13848266
- **Status:** Unknown
- **Last updated:** 2024-09-27T12:28:26.502160+00:00

### Description
(none)

### Used for
(none)

### Input formats
(none)

### Supported languages
(none)

### Supported inputs
(none)

### Properties verified
(none)

### Techniques
(none)

### External tools
(none)

### Examples
(none)

### References
(none)


---
