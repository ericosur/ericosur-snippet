all: \
	apg.class \
	algorithm_para.class \
	HOTPAlgorithm.class \
	TestUuid.class \
	TestBytes.class

clean:
	rm -f *.class

.phony: TestBytes.class


# -o $@

JAVAC=javac

apg.class: apg.java
	$(JAVAC)  $<

algorithm_para.class: algorithm_para.java
	$(JAVAC)  $<

HOTPAlgorithm.class: HOTPAlgorithm.java
	$(JAVAC)  $<

TestUuid.class: TestUuid.java
	$(JAVAC)  $<

StingList.class: StingList.java
	$(JAVAC)  $<

TestBytes.class: TestBytes.java
	$(JAVAC)  $<
