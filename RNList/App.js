/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import MOCK_DATA from './assets/mock_data.json';
import {
  FlatList,
  StatusBar,
  StyleSheet,
  Text,
  View,
} from 'react-native';

import {
  Appbar,
  List,
  Provider as PaperProvider,
} from 'react-native-paper'

class HomePage extends React.Component {

  renderListItem({item}) {
    return <List.Item 
      title={item.title}
      description={item.subtitle}
      />
  }

  render() {
    return (
      <View>
        <Appbar.Header>
          <Appbar.Content title="List"/>
        </Appbar.Header>
        <FlatList
          data={MOCK_DATA}
          renderItem={({item}) => this.renderListItem({item})}
          keyExtractor={item => item.id}
          />
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
});

export default App;
