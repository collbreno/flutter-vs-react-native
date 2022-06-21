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
  Image,
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
      left={props => <Image style={{height: 26, width: 26, alignSelf: 'center', margin: 6}} source={{uri: item.image}}/>}
      right={props => <Text>{item.id}</Text>}
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
