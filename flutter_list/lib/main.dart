import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;

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
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late List<dynamic> items;

  @override
  void initState() {
    super.initState();
    items = [];
    loadItems();
  }

  Future<void> loadItems() async {
    final String response = await rootBundle.loadString('assets/mock_data.json');
    final data = (await json.decode(response)) as List<dynamic>;
    setState(() {
      items = data;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("List"),
      ),
      body: Center(
        child: ListView.builder(
          itemCount: items.length,
          itemBuilder: ((context, index) {
            final item = items[index];
            final image = Uri.parse(item["image"]).data!.contentAsBytes();
            return ListTile(
              leading: CircleAvatar(
                backgroundImage: MemoryImage(image),
                backgroundColor: Colors.transparent,
              ),
              trailing: Text(item["id"].toString()),
              title: Text(item["title"]),
              subtitle: Text(item["subtitle"]),
            );
          }),
        ),
      ),
    );
  }
}
