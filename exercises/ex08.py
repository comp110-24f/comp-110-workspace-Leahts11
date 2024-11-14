"""EX08 - Linked list utils"""

__author__ = "730648923"

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node) -> None:
        """Initializes values."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Makes string representation of linked list."""
        rest: str = "TODO"

        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Find data of node stored at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Find max data value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        return head.value
    max_rest = max(head.next)
    if head.value > max_rest:
        return head.value
    else:
        return max_rest


def linkify(items: list[int]) -> Node | None:
    """Get a linked list of nodes with the same values as the inputted list."""
    if len(items) == 0:
        return None
    node1 = Node(items[0], linkify(items[1:]))
    return node1


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale up/down values in linked list."""
    if head is None:
        return None
    scale_node = Node(head.value * factor, scale(head.next, factor))
    return scale_node
