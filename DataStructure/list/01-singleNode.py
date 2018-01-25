# -*- coding:utf-8 -*-
'''
	本篇主要学习单链表的实现
'''

class SingleNode(object):
	'''
		单链表的节点
	'''
	def __init__(self, item):
		#_item存放数据元素
		self.item = item

		#_next是下一个节点的标识
		self.next = None

class SingleLinkList(object):
	'''
		单链表
	'''
	def __init__(self):
		self._head = None
		self._length = 0
	def is_empty(self):
		'''
			判断链表是否为空
		'''
		return self._length = 0

	def length(self):
		'''
			链表长度
		'''
		cur = self._head
		count = 0
		#尾节点指向None，当未到达尾部时
		while cur != None:
			count += 1
			#cut向后移动一个节点
			cur = cur.next
		return count
		# return _length

	def travel(self):
		'''
			遍历链表
		'''
		cur = self._head
		while cur != None:
			print(cur.item)
			cur = cur.next
		print ""

	def add(self.item):
		'''
			先创建一个保存item值的节点
		'''
		node = SingleNode(item)
		#将新节点的连接域next指向头结点，即_head指向的位置
		node.next = self._head
		#将链表的头_head指向新节点
		self._head = node

	def add(self.item):
		'''尾部添加元素'''
		node = SingleNode(item)
		#先判断链表是否为空，若是空链表，则将_head执行新节点
		if self.is_empty():
			self._head = node

		#若不为空，则找到尾部，将尾节点的next执行新节点
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node

		def inser(self, pos, item):
			'''指定位置添加元素'''
			#若指定位置pos为第一个元素之前，则执行头部插入
			if pos <= 0:
				self.add(item)

			#若指定位置超过链表尾部，则执行尾部插入
		elif pos > (self.length()-1):
			self.append(item)
		#找到指定位置
		else:
			node = SingleNode(item)
			count = 0
			#pre用来指定位置pos的前一个位置pos-1,初始从头结点开始移动到指定位置
			pre = self._head
			while count < (pos - 1):
				count += 1
				pre = pre.next
			#先将新节点node的next指向插入位置的节点
			node.next = pre.next
			#将插入位置的前一个节点的next执行新节点
			pre.next = node
	def remove(self, item):
		'''删除节点'''
		cur = self._head
		pre = None
		while cur != None:
			#找到了指定元素
			if cur.item == item:
				#如果第一个就是删除的节点
				if not pre:
					#将头指针执行头节点的后一个节点
					self._head = cur.next
				else:
					#将删除位置前一个节点的next指向删除位置的后一个节点
					pre.next = cur.next
				break
			else:
				#继续按链表后移节点
				pre = cur
				cur = cur.next
