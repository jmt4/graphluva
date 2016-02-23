import abc

class Graph(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def remove_vertex(self):
		#raise NotImplementedError("Implement me");

	@abc.abstractmethod
	def add_vertex(self):
		return

	@abc.abstractmethod
	def add_edge(self):
		return

	@abc.abstractmethod
	def remove_edge(self):
		return