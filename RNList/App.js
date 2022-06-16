/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import {
  FlatList,
  StyleSheet,
  Text,
  View,
} from 'react-native';

import {
  Appbar,
  List,
  Provider as PaperProvider,
} from 'react-native-paper'

const DATA = [
  {
    id: '1',
    title: 'Banana',
    subtitle: 'Amarela'
  },
  {
    id: '2',
    title: 'Laranja',
    subtitle: 'Laranja'
  },
  {
    id: '3',
    title: 'Maçã',
    subtitle: 'Vermelha'
  },
]

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
          data={DATA}
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
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});

export default App;
