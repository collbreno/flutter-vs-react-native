import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Button,
} from 'react-native';
import {
  Provider as PaperProvider,
  Appbar,
  FAB,
  Portal,
} from 'react-native-paper'
import {
  NavigationContainer,
} from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function HomeScreen({navigation}) {
  return (
    <View style={styles.center}>
      <Text>Home Screen</Text>
      <Button
        title="Go to Details"
        onPress={() => navigation.navigate('Details')}
      />
    </View>
  );
}


function DetailsScreen() {
  return (
    <View style={styles.center}>
      <Text>Details Screen</Text>
    </View>
  );
}

const App = () => {
  return (
    <PaperProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={HomeScreen}/> 
          <Stack.Screen name="Details" component={DetailsScreen}/> 
        </Stack.Navigator>
      </NavigationContainer>
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  center: {
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
  },
})

export default App;