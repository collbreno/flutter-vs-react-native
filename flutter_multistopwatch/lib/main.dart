import 'dart:async';

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  final int milliseconds;

  const HomePage({Key? key})
      : milliseconds = 16,
        super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Counter")),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Holder(milliseconds: milliseconds),
          Holder(milliseconds: milliseconds * 2),
        ],
      ),
    );
  }
}

class Counter extends StatefulWidget {
  final int milliseconds;

  const Counter({Key? key, required this.milliseconds}) : super(key: key);

  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  late int counter;

  @override
  void initState() {
    super.initState();
    counter = 0;
    Timer.periodic(Duration(milliseconds: widget.milliseconds), (timer) {
      setState(() {
        counter += 1;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text(counter.toString());
  }
}

class Holder extends StatelessWidget {
  final int milliseconds;

  const Holder({Key? key, required this.milliseconds}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        Counter(milliseconds: milliseconds),
        Counter(milliseconds: milliseconds),
        Counter(milliseconds: milliseconds),
      ],
    );
  }
}
