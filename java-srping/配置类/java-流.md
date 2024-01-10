流（Stream）是 Java 8 中新增的一个非常强大的功能，它可以极大地简化集合的操作。以下是一些常用的流用法：

1. 遍历元素

使用 `forEach()` 方法可以遍历流中的所有元素。

例如：

```
javaCopy CodeList<String> list = Arrays.asList("apple", "banana", "orange");
list.stream().forEach(System.out::println);
```

上述代码会输出集合中的每个元素。

1. 过滤元素

使用 `filter()` 方法可以根据指定条件过滤流中的元素。

例如：

```
javaCopy CodeList<String> list = Arrays.asList("apple", "banana", "orange");
list.stream().filter(s -> s.startsWith("a")).forEach(System.out::println);
```

上述代码会输出集合中以字母 "a" 开头的元素。

1. 映射元素

使用 `map()` 方法可以将流中的元素映射成另外一种类型。

例如：

```
javaCopy CodeList<String> list = Arrays.asList("apple", "banana", "orange");
list.stream().map(String::toUpperCase).forEach(System.out::println);
```

上述代码会输出集合中所有元素的大写形式。

1. 统计元素数量

使用 `count()` 方法可以统计流中元素的数量。

例如：

```
javaCopy CodeList<String> list = Arrays.asList("apple", "banana", "orange");
long count = list.stream().count();
System.out.println(count);
```

上述代码会输出集合中元素的数量。

1. 求和、平均值、最大值、最小值

使用 `sum()` 方法可以对数值流进行求和操作。

例如：

```
javaCopy CodeIntStream intStream = IntStream.of(1, 2, 3, 4, 5);
int sum = intStream.sum();
System.out.println(sum);
```

上述代码会输出数值流中所有元素的和。

使用 `average()` 方法可以对数值流进行求平均值操作。

例如：

```
javaCopy CodeIntStream intStream = IntStream.of(1, 2, 3, 4, 5);
double average = intStream.average().getAsDouble();
System.out.println(average);
```

上述代码会输出数值流中所有元素的平均值。

使用 `max()` 方法可以对流中的元素进行最大值比较。

例如：

```
javaCopy CodeList<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
int max = list.stream().max(Integer::compareTo).get();
System.out.println(max);
```

上述代码会输出集合中所有元素的最大值。

使用 `min()` 方法可以对流中的元素进行最小值比较。

例如：

```
javaCopy CodeList<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
int min = list.stream().min(Integer::compareTo).get();
System.out.println(min);
```

上述代码会输出集合中所有元素的最小值。

这些只是流操作中的一部分，实际上流还有很多其他的操作，如排序、去重、分组、分区等等。掌握流的使用，可以大大提高 Java 开发效率。