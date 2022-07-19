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

class Holder extends React.Component {
  render() {
    return (
      <View style={styles.column_evenly_spaced}>
        <Counter milliseconds={this.props.milliseconds} />
        <Counter milliseconds={this.props.milliseconds} />
        <Counter milliseconds={this.props.milliseconds} />
      </View>
    )
  }
}

class HomePage extends React.Component {
  constructor(props) {
    super(props)
    this.milliseconds = 16
  }

  render() {
    return (
      <View>
        <Portal>
          <Appbar.Header>
            <Appbar.Content title="Counter" />
          </Appbar.Header>
          <View style={styles.center}>
            <View style={styles.row_evenly_spaced}>
              <Holder milliseconds={this.milliseconds} />
              <Holder milliseconds={this.milliseconds * 2} />
            </View>
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
    flex: 1,
  },
  column_evenly_spaced: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'space-evenly',
  },
  row_evenly_spaced: {
    flex: 1,
    flexDirection: 'row',
    justifyItems: 'space-between',
    justifyContent: 'space-evenly',
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
  },
})

export default App;
