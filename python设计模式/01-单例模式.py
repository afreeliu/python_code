# -*- coding:utf-8 -*-


class Singleton(object):
	def __new__(cls):
		# 关键在于此，每一次实例化的时候，我们都只会返回这同一个instance对象
		if not hasattr(cls, "instance"):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


obj1 = Singleton()
obj2 = Singleton()