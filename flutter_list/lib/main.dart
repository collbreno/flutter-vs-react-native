import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

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
        systemOverlayStyle: const SystemUiOverlayStyle(
          statusBarColor: Colors.black,
          statusBarIconBrightness: Brightness.dark,
        ),
        title: Text("List", style: TextStyle(color: Colors.lightBlue.shade100)),
      ),
      body: Center(
        child: ListView.builder(
          itemCount: items.length,
          itemBuilder: ((context, index) {
            final item = items[index];
            final image = Uri.parse(item["image"]).data!.contentAsBytes();
            return ListTile(
              tileColor: Colors.lightBlue.shade100,
              leading: CircleAvatar(
                backgroundColor: Colors.transparent,
                child: Image.memory(
                  image,
                  width: 26,
                  height: 26,
                  fit: BoxFit.fill,
                ),
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
