/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

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

class HomePage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0,
    }
  }

  incrementCounter() {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <View>
        <Portal>
          <Appbar.Header>
            <Appbar.Content title="Counter" />
          </Appbar.Header>
          <View style={styles.center}>
            <Text style={styles.titleText}>You have pushed the button this many times:</Text>
            <Text style={styles.counterText}>{this.state.count}</Text>
          </View>
          <FAB
            style={styles.fab}
            icon="plus"
            onPress={() => this.incrementCounter()} />
        </Portal>
      </View>
    )
  }
}

const App = () => {
  return (
    <PaperProvider>
        <HomePage />
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  titleText: {
    color: 'black'
  },
  counterText: {
    fontSize: 34,
  },
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
