import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import StarRatingComponent from 'react-star-rating-component';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
}));

export default function SimpleTable(props) {
  const classes = useStyles();
  var rows = []
  for (var key in props.availability){
    rows.push({
      'name': key,
      'calories': props.nutrition[key]?props.nutrition[key]['calories']:'N/A',
      'available': props.availability[key]['available']?'Yes':'No',
      'rating': props.ratings[key]['rating'],
      'count': props.ratings[key]['count']
    })
  }

  return (
    <Paper className={classes.root}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell>Snack</TableCell>
            <TableCell align="right">Calories (kcal) </TableCell>
            <TableCell align="right">Available?</TableCell>
            <TableCell align="right">Popularity</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.name} onClick={() => props.clickAction(row.name)}>
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.available}</TableCell>
              <TableCell align="right" style={{fontSize: 10, textAlign: 'center'}}>
                <StarRatingComponent
                  name={row.name}
                  value={row.rating}
                  editing={false}
                />
                <span style={{}}>
                ({row.count})
                </span>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}
