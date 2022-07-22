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

  renderListItem({ item }) {
    return <List.Item
      style={styles.item}
      title={item.title}
      description={item.subtitle}
      left={props => <Image {...props} style={styles.leading} source={{ uri: item.image }} />}
      right={props => <Text {...props} style={styles.trailing}>{item.id}</Text>}
    />
  }

  render() {
    return (
      <View>
        <StatusBar
          backgroundColor={'black'}
          barStyle={'dark-content'} />
        <Appbar.Header>
          <Appbar.Content title="List" color={"#b3e5fc"} />
        </Appbar.Header>
        <FlatList
          data={MOCK_DATA}
          renderItem={({ item }) => this.renderListItem({ item })}
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
  leading: {
    height: 26,
    width: 26,
    alignSelf: 'center',
    margin: 6,
  },
  trailing: {
    alignSelf: 'center',
  },
  item: {
    backgroundColor: '#b3e5fc',
  },
});

export default App;
