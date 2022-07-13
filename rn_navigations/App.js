import React from 'react';
import {
  View,
  Text,
  StyleSheet,
} from 'react-native';
import {
  Provider as PaperProvider,
  Appbar,
  FAB,
  Portal,
} from 'react-native-paper'
import {
  NavigationContainer
} from '@react-navigation/native'

class HomePage extends React.Component {

  render() {
    return (
      <View>
        <Portal>
          <Appbar.Header>
            <Appbar.Content title="Counter" />
          </Appbar.Header>
          <View>
          </View>
          <FAB
            style={styles.fab}
            icon="plus"
            color="white"
            onPress={() => { }} />
        </Portal>
      </View>
    )
  }
}

const App = () => {
  return (
    <PaperProvider>
      <NavigationContainer>
        <HomePage />
      </NavigationContainer>
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  center: {
    alignItems: 'center',
    justifyContent: 'center',
    height: '100%',
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
  },
})

export default App;