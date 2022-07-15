import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Button,
} from 'react-native';
import {
  NavigationContainer,
} from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Routes = {
  HOME: 'Home',
  FIRST: 'First',
  SECOND: 'Second',
}

const Stack = createNativeStackNavigator();

function HomeScreen({navigation}) {
  return (
    <View style={styles.center}>
      <Text>Home Screen</Text>
      <View style={styles.button}>
        <Button
          title="Navigate"
          onPress={() => navigation.navigate(Routes.FIRST)}
        />
      </View>
      <View style={styles.button}>
        <Button
          title="Navigate again"
          onPress={() => navigation.navigate(Routes.SECOND)}
        />
      </View>
    </View>
  );
}


function FirstScreen({navigation}) {
  return (
    <View style={styles.center}>
      <Text>First Screen</Text>
      <Text>Just a simple screen with some text</Text>
      <View style={styles.button}>
        <Button
          title="Back"
          onPress={() => navigation.pop()}
        />
      </View>
    </View>
  );
}

function SecondScreen({navigation}) {
  return (
    <View style={styles.center}>
      <Text>Second Screen</Text>
      <Text>Just another simple screen with some text</Text>
      <View style={styles.button}>
        <Button
          title="Back"
          onPress={() => navigation.pop()}
        />
      </View>
    </View>
  );
}

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home" screenOptions={{
        animation: 'slide_from_bottom',
        headerStyle: { backgroundColor: '#6200ee' },
        headerTintColor: '#fff',
      }}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="First" component={FirstScreen} />
        <Stack.Screen name="Second" component={SecondScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const styles = StyleSheet.create({
  center: {
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
  },
  button: {
    marginTop: 20,
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
  },
})

export default App;