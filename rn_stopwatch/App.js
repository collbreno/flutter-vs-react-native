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

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0
    }

    setInterval(() => {
      this.setState(prev => ({ counter: prev.counter + 1 }))
    }, this.props.milliseconds);
  }

  render() {
    return (
      <Text>{this.state.counter}</Text>
    )
  }
}

class HomePage extends React.Component {

  render() {
    return (
      <View>
        <Portal>
          <Appbar.Header>
            <Appbar.Content title="Counter" />
          </Appbar.Header>
          <View style={styles.center}>
            <Counter milliseconds={16} />
          </View>
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
